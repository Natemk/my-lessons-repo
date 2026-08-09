from typing import Literal, TypedDict
from math import prod as product
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    operator: Literal["+", "*"]
    values: list
    message: str
    name: str

def calculate_node(state: AgentState) -> AgentState:
    """Node that calculates a list of valuers when given either one of the sum and multiplication literal operators"""
    if state["operator"] == "+":
        answer = sum(state["values"])
    elif state["operator"] == "*":
        answer= product(state["values"])
    else:
        state["message"] = f"Hello {state['name']}, {state['operator']} is not a valid operator please put in a valid operator"
        return state

    state["message"] =f"Hello {state['name']}, your answer is {answer}"
    return state

graph = StateGraph(AgentState)

graph.add_node("calc", calculate_node)

graph.set_entry_point("calc")
graph.set_finish_point("calc")

app=graph.compile()

result = app.invoke(
    {
        "operator": "+",
        "values": [1,2,3,4],
        "message": "",
        "name": "Nate"
    }
)

print(result["message"])



