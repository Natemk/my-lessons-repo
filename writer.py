import os
# writer expects OPENAI_API_KEY to be set in environment by the launcher (app.py)

from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from langgraph.func import entrypoint, task

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Set it in .env before running.")


#model

model = init_chat_model(
    "gpt-3.5-turbo",
    temperature = 0.7,
    api_key=OPENAI_API_KEY,
)

#llm task

@task
def llm_call(messages: list[BaseMessage]):
    """
    Ask the Writer AI to create the requested content.
    
    """
    
    system_message = SystemMessage(
        content="""You are a professional AI writer. Your job is to create high-quality written content based on the user's instructions.

        You can write:

        - Articles
        - Reports
        - Essays
        - Blog posts
        - Stories
        - Scripts
        - Explanations
        - Summaries
        - Other forms of written content

        Follow the user's instructions carefully.

        Writing rules:

        1. Understand what the user is asking for.
        2. Follow the requested format.
        3. Organize the content clearly.
        4. Use natural and readable language.
        5. Avoid unnecessary repetition.
        6. Do not invent facts.
        7. If research is provided, use that research
        as the factual foundation.
        8. Do not change facts from the research.
        9. Match the requested length when possible.
        10. Produce the final content directly.

        If the user provides research from another
        AI agent, use that research to help produce
        the final answer."""
    )

    return model.invoke([
        system_message,
        *messages
    ])

@entrypoint()

def writer(messages: list[BaseMessage]):
    """
    The Writer AI agent. This agent takes in a list of messages and produces the final written content.
    
    """
    
    response = llm_call(messages).result()

    messages = add_messages(messages, response)
    
    return messages 
