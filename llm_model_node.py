from langchain.messages import SystemMessage
from llm_state import MessagesState


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
            model_with_tools.invoke([system_message] + state["messages"])
        ],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }