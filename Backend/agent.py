from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from typing import TypedDict

import os
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE")

class GraphState(TypedDict):
    transcript: str
    query: str
    messages: list
    response: str

llm = ChatOpenAI(
    model="gpt-4.1",
    api_key=OPENROUTER_API_KEY,
    base_url=OPENAI_API_BASE,
    temperature=0.3,
    max_tokens=1024,
    timeout=30
)

MAX_CHARS = 4000

# ✅ Always return full state object
def inject_context(state: GraphState) -> GraphState:
    transcript = state["transcript"][:MAX_CHARS]
    query = state["query"]
    messages = [
        HumanMessage(
            content=(
                "You are an expert video assistant. Based on this transcript (which may be in any language):\n\n"
                f"{transcript}\n\n"
                f"Answer this:\n{query}"
            )
        )
    ]
    return {
        "transcript": transcript,
        "query": query,
        "messages": messages,
        "response": ""
    }

def generate_answer(state: GraphState) -> GraphState:
    response = llm.invoke(state["messages"])
    return {
        "transcript": state["transcript"],
        "query": state["query"],
        "messages": state["messages"],
        "response": response.content
    }

def build_agent():
    builder = StateGraph(GraphState)

    builder.add_node("inject_context", RunnableLambda(inject_context))
    builder.add_node("llm_answer", RunnableLambda(generate_answer))

    builder.set_entry_point("inject_context")
    builder.add_edge("inject_context", "llm_answer")
    builder.add_edge("llm_answer", END)

    return builder.compile()