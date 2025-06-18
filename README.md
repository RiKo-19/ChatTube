# ChatTube
Welcome to the YouTube AI Assistant repository! This project combines a Chrome extension and a FastAPI backend to let users ask intelligent questions about any YouTube video they're watching. It extracts the video's transcript and uses OpenAI via OpenRouter to provide reliable, context-aware answers — all within the extension popup.

---

## About the Project
We developed this assistant to simplify the experience of understanding video content on YouTube. Using a Chrome extension, the tool automatically detects the currently open video and sends its transcript to a FastAPI backend. The backend leverages `youtube-transcript-api` to extract subtitles and uses LangGraph + OpenRouter to query an advanced LLM.

Users can ask questions like "What is this video about?" or "What are the key points mentioned?" and receive concise, AI-generated answers without switching tabs or copying links.

---

## Features
- Ask questions about any YouTube video without leaving the page
- Automatically fetches the current video URL from your browser
- Extracts transcript (manual or auto-generated) using `youtube-transcript-api`
- Sends the transcript and your query to an LLM (via LangGraph + OpenRouter API)
- Backend built with FastAPI, frontend with standard Chrome Extension tools

---

## Technologies Used

### *Programming Language:*
- Python
- JavaScript (for extension frontend)

### *Python Libraries:*
- fastapi
- uvicorn
- python-dotenv
- youtube-transcript-api
- langgraph
- langchain
- langchain-openai

```bash
pip install fastapi uvicorn python-dotenv youtube-transcript-api langgraph langchain langchain-openai
```

### *Frontend Tools:*
- HTML
- JavaScript
- Chrome Extension APIs

### *Other Tools:*
- VS Code
- OpenRouter API (for LLM access)

---

## *Setup Instructions

### ✅ *1. Clone the Repository*

```bash
git clone https://github.com/RiKo-19/ChatTube.git
cd ChatTube
```

### ✅ *2. Backend Setup*
- Create and activate a virtual environment

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Create `.env` file

```bash
OPENROUTER_API_KEY=your_api_key_here
OPENAI_API_BASE=https://openrouter.ai/api/v1
```

- Start the FastAPI server

```bash
uvicorn main:app --reload
```

### ✅ *3. Chrome Extension Setup*
- Load the extension
1. Go to chrome://extensions
2. Enable Developer Mode
3. Click "Load unpacked"
4. Select the extension/ folder

- How it works
1. Open any YouTube video
2. Click on the extension icon
3. Ask a question about the video
4. It will show a smart answer based on the transcript

---

## 🖥️ User Interface

![Screenshot 2025-06-17 233745](https://github.com/user-attachments/assets/65e01662-eda6-4218-b4e8-a5ba97a21e38)
