"""
from typing import TypedDict

class Vision(TypedDict):
    context : str
    search_strategy: str
    number_of_results: int

vision=Vision(context="I want to learn about Python programming.", search_strategy="Use online tutorials and documentation.", number_of_results=5)

def llm_call(vision: Vision) -> str:
    # Simulating a call to a language model with the provided vision
    return f"Context: {vision['context']}\nSearch Strategy: {vision['search_strategy']}\nNumber of Results: {vision['number_of_results']}"

llm_call_response = llm_call(vision)

print(llm_call_response)


from numpy.f2py.crackfortran import f

from typing import Union

def square(x: Union[str, int]) -> float:
    return x * x

x =5
x = 1.778
x = "Hello"

print(square(x))
"""
"""
from typing import Optional

def nice_message(name: Optional[str]) -> None:
    if name is None:
        return ("Hello, Guest!")
    else:
        return (f"Hello, {name}!")

name = nice_message(None)

print(name)
"""



