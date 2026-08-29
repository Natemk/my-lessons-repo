
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
 
# Load environment variables from a local .env file if present
load_dotenv()

# Import the actual agent objects (entrypoints), not the modules.
# `import researcher` / `import writer` would import the *module*, which has
# no .invoke() of its own -- that raised AttributeError as soon as a route
# other than "unknown" fired.
from researcher import research_agent
from writer import writer as writer_agent




OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise SystemExit(
        "OPENAI_API_KEY not found. Create a .env file with OPENAI_API_KEY=your_key "
        "or set it in your shell environment, then rerun."
    )
 
 
VALID_ROUTES = {"research", "write", "research_and_write"}
 
# Small/cheap model used only for classification -- this doesn't need to be
# the same model doing the actual research/writing work. Lazily built so
# importing app.py doesn't require a key before load_dotenv() has run.
_router_model = None

#When u route it allows one to access a certain endpoint from a module
 
def _get_router_model():
    global _router_model
    if _router_model is None:
        _router_model = init_chat_model(
            "gpt-5-mini",
            #temperature=0,
        )
    return _router_model
 
 
ROUTER_SYSTEM_PROMPT = """You are an intent classifier for a two-agent system: a research agent and a writer agent.
 
Classify the user's request into exactly ONE of these routes:
 
- "research": the user wants information found/looked up/summarized (facts, current events, data, analysis of existing information). No new original content needs to be composed.
- "write": the user wants original content composed (essay, story, script, email, blog post, etc.) and does NOT need external facts looked up first.
- "research_and_write": the user wants written content that depends on facts, data, or current information that must be looked up first (e.g. "write a report on X", "draft a blog post about the latest Y").
 
Respond with ONLY one of these exact strings and nothing else: research, write, research_and_write"""
 
 
def route_request(request: str) -> str:
    """
    Decide what the user wants using the LLM instead of keyword matching.
    Keyword lists can't cover every phrasing (a bare factual question like
    "2026 fifa world cup winners" matched nothing before) -- letting the
    model classify intent handles paraphrasing and mixed intent naturally.
    """
    try:
        response = _get_router_model().invoke([
            SystemMessage(content=ROUTER_SYSTEM_PROMPT),
            HumanMessage(content=request),
        ])
        route = response.content.strip().lower()
    except Exception:
        # Classifier itself failed (network, auth, etc.) -- degrade to the
        # safest default rather than raising out of route_request.
        return "research"
 
    if route in VALID_ROUTES:
        return route
 
    # Model didn't return a clean match (rare with temperature=0, but
    # possible) -- default to research rather than refusing outright,
    # since most ambiguous queries are informational.
    return "research"
 
 
# Helper
 
def get_final_response(result) -> str:
    """Get the final AI message from an agent result.

    Handles several possible result shapes from LangGraph/LangChain:
    - list[BaseMessage]
    - single BaseMessage
    - dicts containing messages
    Falls back to str(result) so we never silently print nothing.
    """
    if not result:
        return ""

    # If it's already a single message-like object
    if hasattr(result, "content") and not isinstance(result, list):
        content = result.content
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts = [
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            ]
            return "\n".join(parts) if parts else str(content)
        return str(content)

    # If it's a list, assume it's a list of messages and take the last
    if isinstance(result, list) and result:
        final_message = result[-1]
        content = getattr(final_message, "content", final_message)
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts = [
                block.get("text", "")
                for block in content
                if isinstance(block, dict) and block.get("type") == "text"
            ]
            return "\n".join(parts) if parts else str(content)
        return str(content)

    # If it's a dict, try common keys or just stringify
    if isinstance(result, dict):
        for key in ("messages", "output", "outputs", "result", "text"):
            if key in result and result[key]:
                return get_final_response(result[key])
        return str(result)

    # Fallback: never return an empty string silently
    return str(result)
 
 
# Research only
 
def run_research(request: str) -> str:
    """Run the research agent and return the final response."""
    messages = [HumanMessage(content=request)]
    result = research_agent.invoke(messages)
    return get_final_response(result)
 
 
# Write only
 
def run_write(request: str) -> str:
    """Run the writer agent and return the final response."""
    messages = [HumanMessage(content=request)]
    result = writer_agent.invoke(messages)
    return get_final_response(result)
 
 
# Main orchestration
 
def handle_request(request: str) -> str:
    """Main application function.
 
    The App receives the user's request,
    decides which agent should handle it,
    and sends the request to that agent.
    """
    route = route_request(request)
 
    if route == "research":
        return run_research(request)
 
    elif route == "write":
        return run_write(request)
 
    elif route == "research_and_write":
        research_result = run_research(request)
        combined_request = f"{request}\n\nResearch findings:\n{research_result}"
        return run_write(combined_request)
 
    else:
        # route_request now always returns one of VALID_ROUTES (or falls
        # back to "research" on failure), so this branch shouldn't be
        # reachable -- kept only as a defensive fallback.
        return "I'm not sure how to handle that request. Please specify if you want research or writing"
 
 
if __name__ == "__main__":
 
    print("=" * 50)
    print("AI RESEARCHER / WRITER")
    print("=" * 50)
    print("Type 'exit' to quit.\n")
 
    while True:
 
        user_input = input("You: ")
 
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
 
        response = handle_request(user_input)
 
        print("\nAI:")
        print(response)
        print()