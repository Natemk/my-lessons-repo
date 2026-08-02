#pip install langgraph langchain ipykernel 
# pip install -U langchain-openai

from dotenv import load_dotenv #pip install dotenv and then in your root directory you create a directory named .env after creating it you will see a gear icon next to this directory. This is the directory we keep our secrets i.e env variables
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
import getpass
import os

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter you API Key: ")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    # stream_usage=True,
    # temperature=None,
    # max_tokens=None,
    # timeout=None,
    # reasoning_effort="low",
    # max_retries=2,
    # api_key="...",  # If you prefer to pass api key in directly
    # base_url="...",
    # organization="...",
    # other params...
)

class State(TypedDict):
    name: str
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    """Chatbot node or function that processes user messages"""
    return {"messages": llm.invoke(state["messages"])}

graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

app= graph.compile()

user_input = input("message:")

state = app.invoke(
    {
        "messages": [{"role": "user", "content": user_input}]
    }
)

#print(state["messages"])
print(state["messages"][-1].content)

