import os
import re
from datetime import date
from urllib.parse import quote_plus

import requests
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.graph import add_messages
from langchain.messages import SystemMessage
from langchain_core.messages import BaseMessage, ToolMessage, AIMessage
from langgraph.func import entrypoint, task

try:
    from firecrawl import FirecrawlApp
except ImportError:
    from firecrawl import Firecrawl as FirecrawlApp


# Require OPENAI_API_KEY from environment (app.py should load .env first)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Firecrawl configuration (for search + scraping)
FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
firecrawl_app = None

# Model is initialized lazily so tools can be imported/used without an API key.
model = None
model_with_tools = None

# Safety cap on agent tool-call loops so a confused model can't loop forever.
MAX_TURNS = 6

# Keywords that signal a query is about something current/recent, so we can
# tighten the search freshness window instead of always using one fixed value.
_RECENCY_KEYWORDS = (
    "latest", "recent", "current", "today", "now",
    "breaking", "update", "news"
)

DEBUG = os.environ.get("RESEARCHER_DEBUG") == "1"
# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

def clean_html(html: str) -> str:
    html = re.sub(r"(?si)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", html).strip()


_JUNK_LINK_SUBSTRINGS = (
    "duckduckgo.com",
    "google.com/search",
    "bing.com",
    "facebook.com",
    "linkedin.com",
    "instagram.com",
    "twitter.com",
    "x.com",
)

# Phrases that indicate Firecrawl "succeeded" but actually just captured a
# site's own error/placeholder page rather than real content -- these look
# like a success (no exception raised) but the text is worthless.

_JUNK_CONTENT_MARKERS = (
    "oops, something went wrong",
    "page not found",
    "404 error",
    "access denied",
    "please enable javascript",
    "just a moment...",  # Cloudflare challenge page
    "checking your browser",
)


def _looks_like_junk_page(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in _JUNK_CONTENT_MARKERS)


def _get_firecrawl_app():
    """Lazily initialize and return the global Firecrawl client."""
    global firecrawl_app, FIRECRAWL_API_KEY
    if firecrawl_app is None:
        FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
        if not FIRECRAWL_API_KEY:
            raise RuntimeError(
                "FIRECRAWL_API_KEY not found in environment. Set it in .env before running."
            )
        firecrawl_app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
    return firecrawl_app


def _pick_tbs(query: str) -> str:
    """Pick a freshness window based on the query itself, instead of a fixed one."""
    q = query.lower()
    if any(kw in q for kw in _RECENCY_KEYWORDS):
        return "qdr:w"  # past week — tight window for time-sensitive queries
    return "qdr:y"  # past year — broad enough not to exclude normal queries


@tool
def web_search(query: str) -> str:
    """Searches the web and returns the top result URL, prioritizing recent content."""
    try:
        app = _get_firecrawl_app()
        result = app.search(
            query,
            limit=5,
            tbs=_pick_tbs(query),
        )

        items = []
        if hasattr(result, "web") and result.web:
            items = result.web
        elif isinstance(result, dict) and result.get("web"):
            items = result["web"]
        elif isinstance(result, list):
            items = result

        for item in items:
            link = item.get("url") if isinstance(item, dict) else getattr(item, "url", None)
            if link and not any(junk in link.lower() for junk in _JUNK_LINK_SUBSTRINGS):
                return link

        return "No search results found."
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"

@tool
def scrape_page(url: str) -> str:
    """Scrapes text content from a web page using Firecrawl."""
    try:
        app = _get_firecrawl_app()
        # Confirmed by Firecrawl's own docs: .scrape(url, formats=[...]) —
        # no params= dict, result is an object with a .markdown attribute.
        result = app.scrape(url, formats=["markdown"])

        text = getattr(result, "markdown", None)
        if text is None and isinstance(result, dict):
            text = result.get("markdown")

        if not text:
            return f"Firecrawl returned no markdown content for {url}. Raw response: {str(result)[:500]}"

        if _looks_like_junk_page(text[:500]):
            return f"ERROR: scraped content from {url} appears to be an error/placeholder page, not real content."

        snippet = text[:3000]
        return f"Scraped via Firecrawl from {url}: {len(snippet)} chars extracted.\n\n{snippet}"
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
        model = init_chat_model(
            "gpt-4o-mini",
            temperature=0.3,
            api_key=OPENAI_API_KEY,
        )
        model_with_tools = model.bind_tools(tools)
    return model_with_tools


def _build_system_message() -> SystemMessage:
    return SystemMessage(
        content=(
            f"Today's date is {date.today().isoformat()}. When a query concerns whether "
            "something is current, recent, or still true, treat this date as ground truth "
            "and prioritize sources published close to it.\n\n"
            "You are a research agent. Your job is to find accurate, up-to-date information. "
            "When a query requires external information, follow this workflow:\n"
            "1) Call the `web_search` tool with a short search query.\n"
            "2) If `web_search` returns a URL, call `scrape_page` with that URL to extract page text.\n"
            "3) Use the scraped text to produce a concise factual summary and cite the source URL.\n"
            "Do not invent facts. Prefer authoritative sources (news, government, academic, major publications).\n"
            "If search or scraping fails (e.g. status errors, captchas, no text extracted), include those error "
            "messages in your answer instead of only saying 'no reliable web results found'.\n"
            "If web_search and scrape_page run but return no usable information, say plainly that you could not "
            "verify the answer with a live search — do not answer from your own prior/training knowledge on the topic."
        )
    )


# ---------------------------------------------------------------------------
# Agent graph
# ---------------------------------------------------------------------------

@task
def llm_call(messages: list[BaseMessage]):
    """LLM decision whether to call a tool or not."""
    return get_model_with_tools().invoke([_build_system_message(), *messages])


@task
def call_tool(tool_call):
    """Invoke a tool and wrap the result in a ToolMessage."""
    t = tools_by_name[tool_call["name"]]
    observation = t.invoke(tool_call.get("args", {}))
    # Silently log tool activity to a file for troubleshooting.
    # Nothing is ever printed to the terminal — your screen stays clean.
    try:
        with open("debug.log", "a", encoding="utf-8") as f:
            f.write(f"tool={tool_call['name']} args={tool_call.get('args', {})}\n")
            f.write(f"result: {str(observation)[:500]}\n\n")
    except Exception:
        pass  # never let logging itself break the app
    return ToolMessage(
        content=str(observation),
        tool_call_id=tool_call["id"],
    )

@entrypoint()
def research_agent(messages: list[BaseMessage]):
    model_response = llm_call(messages).result()
    sources: list[str] = []

    turns = 0
    while model_response.tool_calls and turns < MAX_TURNS:
        tool_result_futures = [
            call_tool(tool_call) for tool_call in model_response.tool_calls
        ]
        tool_results = [f.result() for f in tool_result_futures]

        for tc, tr in zip(model_response.tool_calls, tool_results):
            if tc["name"] == "scrape_page" and tr.content.startswith("Scraped via Firecrawl"):
                url = tc.get("args", {}).get("url")
                if url and url not in sources:
                    sources.append(url)

        messages = add_messages(messages, [model_response, *tool_results])
        model_response = llm_call(messages).result()
        turns += 1

    if model_response.tool_calls:
        forced = SystemMessage(
            content=(
                "You have used all available search attempts. Based on whatever information "
                "you found (or state plainly that you found none), give the user a direct final "
                "answer now. Do not call any more tools."
            )
        )
        model_response = get_model_with_tools().invoke([*messages, forced])

    if sources:
        source_lines = "\n".join(f"- {s}" for s in sources)
        final_text = f"{model_response.content}\n\nSources:\n{source_lines}"
        model_response = AIMessage(content=final_text)

    messages = add_messages(messages, [model_response])
    return messages

# Backwards-compatible export
researcher = research_agent