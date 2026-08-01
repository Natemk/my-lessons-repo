from typing import TypedDict, List, Literal
from langgraph.graph import StateGraph
from math import prod as Product

class AgentState(TypedDict):
    message: str
    values: List[int]
    operation: Literal["*", "+"]
    name: str

def calc_node(state: AgentState) -> AgentState:
    if state["operation"] == "+":
        answer = sum(state["values"])
    elif state["operation"] == "*":
        answer = Product(state["values"])
        return state
    else:
        state["message"] = f"{state['name']} please provide a valuable operator"
        return state

    state["message"] = f"{state['name']} your answer is {answer}"
    return state

#create graph

graph = StateGraph(AgentState)

#Initialise graph

graph.add_node("calc", calc_node)

graph.set_entry_point("calc")
graph.set_finish_point("calc")

app = graph.compile()

message = app.invoke({
    "name": "Greg",
    "operation": "+",
    "values": [1,1,1,1,1],
    "message":""
})

print(message["message"])


