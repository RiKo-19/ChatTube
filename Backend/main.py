from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.transcript import get_transcript
from app.agent import build_agent

app = FastAPI()

# ✅ YOUR EXTENSION ORIGIN — replace with the exact ID shown in the error
EXTENSION_ORIGIN = "chrome-extension://ehlnpfcjcalccnjondlokficpbkiefdk"

# ✅ CORS middleware must be declared BEFORE any routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[EXTENSION_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent_graph = build_agent()

class VideoRequest(BaseModel):
    video_url: str
    query: str

@app.post("/chat")
def chat_with_video(req: VideoRequest):
    transcript = get_transcript(req.video_url)

    if transcript.startswith("Error"):
        return {"error": transcript}

    result = agent_graph.invoke({
        "transcript": transcript,
        "query": req.query,
        "messages": [],
        "response": ""
    })

    return {"answer": result["response"]}
