from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict): #state schema
    message: str

def compliment_node(state: AgentState) -> AgentState:
    """A simple node that takes a message from state and adds a compliment to it"""
    state["message"] = state["message"]  + ", you're doing an amazing job learning langgraph!"
    return state

graph=StateGraph(AgentState)

graph.add_node("compliment", compliment_node)

graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app=graph.compile()

result=app.invoke({"message": "Bob"})  # Output: {'message': 'Bob, you're doing an amazing job learning langgraph!'}

print(result["message"])


