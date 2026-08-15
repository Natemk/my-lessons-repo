import os
import re
from urllib.parse import quote_plus
 
import requests
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.graph import add_messages
from langchain.messages import SystemMessage
from langchain_core.messages import BaseMessage
from langgraph.func import entrypoint, task
 
 
# Require OPENAI_API_KEY from environment (app.py should load .env first)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
 
# Model is initialized lazily so web search and scrape tools can be imported and used without an API key.
model = None
model_with_tools = None
 
# Safety cap on agent tool-call loops so a confused model can't loop forever
# (burning API cost / hanging the CLI).
MAX_TURNS = 6
 
 
# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------
 
def clean_html(html: str) -> str:
    html = re.sub(r"(?si)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html).strip()
 
 
# Links that show up in DuckDuckGo's HTML result page but are never the
# actual top organic result. The old code's "first http(s) link that isn't
# duckduckgo.com" logic frequently grabbed one of these instead of a real
# result.
_JUNK_LINK_SUBSTRINGS = (
    "duckduckgo.com",
    "duckduckgo.com/y.js",  # ad redirect
    "google.com/search",
    "bing.com",
    "heraldonline.co.zw"
)
 

@tool
def web_search(query: str) -> str:
    """Searches the web and returns the top result URL."""
    try:
        url = f"https://duckduckgo.com/html/?q={quote_plus(query)}"
        resp = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
                "Referer": "https://duckduckgo.com/",
            },
            timeout=15,
        )
        if resp.status_code != 200:
            return f"Search failed with status {resp.status_code}"
 
        # DuckDuckGo's HTML result page marks organic result links with the
        # class "result__a". Anchor on that instead of "first http link we
        # see", which was catching ads/nav links before the real result.
        result_links = re.findall(
            r'<a[^>]+class="result__a"[^>]+href=["\'](https?://[^"\']+)["\']',
            resp.text,
            flags=re.I,
        )
        for link in result_links:
            if not any(junk in link.lower() for junk in _JUNK_LINK_SUBSTRINGS):
                return link
 
        # Fallback: DDG sometimes wraps results in a redirect link
        # (/l/?uddg=<encoded real url>) instead of a direct href.
        redirect_match = re.search(
            r'href=["\'](/l/\?uddg=[^"\']+)["\']', resp.text, flags=re.I
        )
        if redirect_match:
            return f"https://duckduckgo.com{redirect_match.group(1)}"
 
        return "No search results found."
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"
 
 
@tool
def scrape_page(url: str) -> str:
    """Scrapes text content from a web page."""
    try:
        resp = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
            },
            timeout=15,
        )
        if resp.status_code != 200:
            return f"Page fetch failed with status {resp.status_code}"
 
        text = clean_html(resp.text)
        if not text:
            return f"Page loaded from {url} but no text could be extracted."
 
        snippet = text[:3000]
        return f"Scraped {url}: {len(snippet)} chars extracted.\n\n{snippet}"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"
 
 
tools = [web_search, scrape_page]
 
tools_by_name = {t.name: t for t in tools}
 
 
def get_model_with_tools():
    global model, model_with_tools, OPENAI_API_KEY
    if model_with_tools is None:
        OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise RuntimeError(
                "OPENAI_API_KEY not found in environment. Set it in .env before running."
            )
 
        # gpt-3.5-turbo is deprecated and noticeably weaker at multi-step
        # tool orchestration. gpt-4o-mini is a comparably cheap but far more
        # reliable choice for a research/tool-calling loop.
        model = init_chat_model(
            "gpt-4o-mini",
            temperature=0.3,
            api_key=OPENAI_API_KEY,
        )
        model_with_tools = model.bind_tools(tools)
    return model_with_tools
 
 
# ---------------------------------------------------------------------------
# Agent graph
# ---------------------------------------------------------------------------
 
@task
def llm_call(messages: list[BaseMessage]):
    """LLM decision whether to call a tool or not.
 
    Args:
        messages: List of messages in the conversation.
    """
    system_message = SystemMessage(
        content=(
            "You are a research agent. Your job is to find accurate, up-to-date information. "
            "When a query requires external information, follow this workflow:\n"
            "1) Call the `web_search` tool with a short search query.\n"
            "2) If `web_search` returns a URL, call `scrape_page` with that URL to extract page text.\n"
            "3) Use the scraped text to produce a concise factual summary and cite the source URL.\n"
            "Do not invent facts. Prefer authoritative sources (news, government, academic, major publications). "
            "If no useful web results exist, say 'no reliable web results found'."
        )
    )
 
    return get_model_with_tools().invoke([system_message, *messages])
 
 
@task
def call_tool(tool_call):
    t = tools_by_name[tool_call["name"]]
    return t.invoke(tool_call)
 
 
@entrypoint()
def research_agent(messages: list[BaseMessage]):
    model_response = llm_call(messages).result()
 
    turns = 0
    while model_response.tool_calls and turns < MAX_TURNS:
        tool_result_futures = [
            call_tool(tool_call) for tool_call in model_response.tool_calls
        ]
        tool_results = [f.result() for f in tool_result_futures]
 
        messages = add_messages(messages, [model_response, *tool_results])
        model_response = llm_call(messages).result()
        turns += 1
 
    messages = add_messages(messages, [model_response])
    return messages
 
 
# Backwards-compatible export: allow `from researcher import researcher`
researcher = research_agent
 