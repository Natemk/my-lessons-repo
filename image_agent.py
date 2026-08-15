import os #read/write environment variables,  in this case the API Key
import base64 #encodes raw image bytes to text-safe characters
import getpass
from pathlib import Path
from typing import TypedDict, Optional, List
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

model = ChatOpenAI(model="gpt-4o")

def encode_image(image_path: str) -> tuple[str, str]:
    """
    Take: a file path (string), e.g "photo.jpg"
    Returns: a tuple of (base64_string, mime_type)
    
    """
    path = Path(image_path)
    ext = path.suffix.lower().lstrip(".")
    mime_type = f"image/{'jpeg' if ext == 'jpg' else ext}"
    
    with open(path, "rb") as f:
        b64_string = base64.b64encode(f.read()).decode("utf-8")
    return b64_string, mime_type


class AgentState(TypedDict):
    image_path: str
    user_text: Optional[str]
    system_prompt: Optional[str]
    messages: List[dict]
    result: Optional[str]
    
    
DEFAULT_SYSTEM_PROMPT =(
    "You are a meticulous visual analyst. Look at the provided image thoroughly and describe what is relavant, factual and useful about it."
)

def build_message(state: AgentState) -> AgentState:
    b64_data, mime_type = encode_image(state["image_path"])

    user_text = state.get("user_text")
    prompt_text = user_text if user_text else "Analyze this image."

    # include the image as a data URL in the human message content
    image_data_url = f"data:{mime_type};base64,{b64_data}"
    human_content = f"{prompt_text}\n\nImage: {image_data_url}"

    human_message = HumanMessage(content=[
    {"type": "text", "text": prompt_text},
    {"type": "image_url", "image_url": {"url": image_data_url}},])
    state["messages"] = [
        SystemMessage(content=state.get("system_prompt") or DEFAULT_SYSTEM_PROMPT),
        human_message,
    ]

    return state

model = ChatOpenAI(model="gpt-4o")


def call_model(state: AgentState) -> AgentState:
    response = model.invoke(state["messages"])
    state["result"] = response.content
    return state



def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("build_message", build_message)
    graph.add_node("call_model", call_model)
    graph.add_edge(START, "build_message")
    graph.add_edge("build_message", "call_model")
    graph.add_edge("call_model", END)
    return graph.compile()


app = build_graph()

if __name__ == "__main__":
    
    image_path = input("Drag an image file here and press Enter: ").strip().strip('"').strip('"')
    user_text = input("Ask something about the image (or press Enter to skip): ").strip() or None
    #  image + explicit user text -> text drives the answer
    result = app.invoke({
        "image_path": image_path,
        "user_text": user_text,
        "system_prompt": DEFAULT_SYSTEM_PROMPT,
    })
    print(result["result"])

   