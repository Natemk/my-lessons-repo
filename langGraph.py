from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict): # Our state schema
    message : str

def greeting_node (state: AgentState) -> AgentState:
    """A simple node that takes a message from state and adds a greeting to it"""
    state["message"]= "Hello," + state["message"] + ", Welcome to the game of LangGraph!"
    return (state)

graph=StateGraph(AgentState)

graph.add_node("greeter", greeting_node)

graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app=graph.compile()

#from IPython.display import display, Image  # noqa: E402
#display(Image(app.get_graph().draw_mermaid_png()))

#with open("langgraph.png", "wb") as f:
#    f.write(app.get_graph().draw_mermaid_png()) 

result=app.invoke({"message": "User"})  # Output: {'message': 'Hello, User, Welcome to the game of LangGraph!'}
print(result["message"])
