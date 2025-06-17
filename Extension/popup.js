document.getElementById("submit").addEventListener("click", async () => {
  const query = document.getElementById("query").value;
  const answerDiv = document.getElementById("answer");

  answerDiv.innerText = "Processing...";

  chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
    const url = tabs[0].url;

    if (!url.includes("youtube.com/watch")) {
      answerDiv.innerText = "Please open a YouTube video.";
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ video_url: url, query: query })
      });

      const data = await response.json();
      if (data.answer) {
        answerDiv.innerText = data.answer;
      } else if (data.error) {
        answerDiv.innerText = "Error: " + data.error;
      } else {
        answerDiv.innerText = "Unexpected response.";
      }
    } catch (err) {
      answerDiv.innerText = "Failed to fetch: " + err.message;
    }
  });
});
