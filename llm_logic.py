from typing import Literal
from langgraph import StateGraph, START, END

def should_continue(state: MessageState) -> Literal["tool_node", END]:
    """Determines whether to continue the loop or stop based upon whether the LLM made a tool call."""
    
    messages = state["messages"]
    last_message = messages[-1]
    
    #If the last message is a tool call, action is then performed
    if last_message.tool_calls:
        return "tool_node"
    
    #Otherwise, the loop is complete and we can end
    