import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    load_dotenv = None

from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator
from langchain.messages import ToolMessage
from langchain.messages import SystemMessage
from typing import Literal
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display
from langchain.messages import HumanMessage

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    OPENAI_API_KEY = input("Enter your OpenAI API key: ")
    if not OPENAI_API_KEY.strip():
        raise RuntimeError(
            "OpenAI API key is required. Run the script again and enter your key when prompted."
        )

model = init_chat_model(
    "gpt-3.5-turbo",
    temperature=0,
    api_key=OPENAI_API_KEY,
)

#Define tools
@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers, 'a' and 'b'.
    
    Args:
        a: First float
        b: Second float"""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divides two numbers, 'a' and 'b'.
    
    Args:
        a: First float
        b: Second float"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def add(a: float, b: float) -> float:
    """Adds two numbers, 'a' and 'b'.
    
    Args:
        a: First float
        b: Second float"""
    return a + b

# Aurgment the LLM with tools
tools = [multiply, divide, add]
tools_by_name = {tool.name: tool for tool in tools}
tool_names = [tool.name for tool in tools]
model_with_tools = model.bind_tools(tools)

#Step 2: Defining the state 



class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int
    
#Step 3: Define the LLM node




def llm_call(state: MessagesState, model_with_tools):
    """LLM decision whether to call a tool or not

    Args:
        state: Messages state containing a "messages" list.
        model_with_tools: an object with an invoke(list[messages]) method.
    """

    system_message = SystemMessage(
        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
    )

    return {
        "messages": [
            model_with_tools.invoke(
                [
                    system_message := SystemMessage(
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }
    
#step 4: Define the tool node



def tool_node(state: MessagesState):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

#Step 5: Define the logic for routing between the LLM and tool nodes



def should_continue(state: MessagesState) -> str:
    """Determines whether to continue the loop or stop based upon whether the LLM made a tool call."""
    
    messages = state["messages"]
    last_message = messages[-1]
    
    #If the last message is a tool call, action is then performed
    if last_message.tool_calls:
        return "tool_node"
    
    #Otherwise, the loop is complete and we can end
    return END

#Step 6: Build agent

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)

agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()


# Show the agent
display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

## Invoke

messages = [HumanMessage(content="What is 3 + 4?")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
