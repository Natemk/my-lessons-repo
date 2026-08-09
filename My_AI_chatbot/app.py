import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the repository root and ensure OPENAI_API_KEY is set
load_dotenv(Path(__file__).resolve().parents[1] / ".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise SystemExit("OPENAI_API_KEY not found in .env at project root")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain.messages import HumanMessage

from My_AI_chatbot.researcher import researcher
from My_AI_chatbot.writer import writer

# Router

def route_request(request: str) -> str:
    """
    Decide what the user wants.
    
    Possible routes:
    
    research
    write
    research_and_write
    unknown
    
    """
    
    text =request.lower()
    
    research_words = [
        "research",
        "find",
        "look up",
        "search",
        "investigate",
        "explore",
        "analyze",
        "study",
        "examine",
        "gather information",
        "collect data",
        "dig into",
        "get information",
    ]
    
    writing_words = [
        "write",
        "compose",
        "draft",
        "create",
        "generate",
        "produce",
        "develop",
        "formulate",
        "construct",
        "put together",
    ]
    
    needs_research = any(
        word in text 
        for word in research_words
    )
    
    needs_writing = any(
        word in text 
        for word in writing_words
    )
    
    # Determine the route based on the presence of research and writing keywords
    if needs_research and needs_writing:
        return "research_and_write"
    
    elif needs_research:
        return "research"
    
    elif needs_writing:
        return "write"
    
    else:
        return "unknown"


# Helper

def get_final_response(result) -> str:
    """Get the final AI maessage from an agent result."""
    if not result:
        return ""
    final_message = result[-1]
    return final_message.content


# Research only

def run_research(request: str) -> str:
    """Run the research agent and return the final response."""
    messages = [HumanMessage(content=request)]
    result = researcher.invoke(messages)
    return get_final_response(result)


# Write only

def run_write(request: str) -> str:
    """Run the writer agent and return the final response."""
    messages = [HumanMessage(content=request)]
    result = writer.invoke(messages)
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

        response = handle_request(
            user_input
        )

        print("\nAI:")
        print(response)
        print()