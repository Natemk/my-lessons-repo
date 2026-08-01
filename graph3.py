from typing import TypedDict, List
from langgraph.graph import StateGraph
from math import prod as product

class AgentState(TypedDict): #state schema
    values: List[int]
    name: str
    operation: str
    result: str

def calculation_node(state: AgentState) -> dict:
    """A simple node that takes a list of values and an operation from state and performs the calculation"""
    if state["operation"] == "+":
        answer = sum(state["values"])
    elif state["operation"] == "*":
        answer = product(state["values"])
    else:
        return {
            "result": f"Hi {state['name']}, the operation you provided is not supported."
        }
    return {
        "result": f"Hi {state['name']}, the result of the operation {state['operation']}  is {answer}."
    }


graph=StateGraph(AgentState)


graph.add_node("calculation", calculation_node)
graph.set_entry_point("calculation")
graph.set_finish_point("calculation")

app=graph.compile()

result = app.invoke({
    "values": [1, 2, 3, 4], 
    "name": "Nyasha", 
    "operation": "*", 
    "result": ""
    })  # Output: {'message': 'Hi Alice, the result of the operation + on the values [1, 2, 3, 4] is 10.'
    

print(result["result"])