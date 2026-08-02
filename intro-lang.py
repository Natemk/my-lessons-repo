from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict): # this is our schema
    message : str
    name : str
    age : int

def greeting_node(state: AgentState) -> AgentState:
    """A simple node that takes a message from state and add a greeting to it"""
    state["message"] = f"Hello {state['name']}, you are aged {state["age"]}years and  welcome to langgraph"
    return state

graph=StateGraph(AgentState)

#Create our graph

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app=graph.compile()

result=app.invoke(
{
        "message":"",
        "name": "Nate",
        "age": 25 
      }
)

print(result["message"])

#with open("Nates_first_node.png", "wb") as f:
#     f.write(app.get_graph().draw_mermaid_png())