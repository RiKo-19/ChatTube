from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript

def get_video_id(video_url: str) -> str:
    import re
    # Handles watch?v=, youtu.be/, and shorts/
    patterns = [
        r"v=([^&]+)",                  # youtube.com/watch?v=xxxx
        r"youtu\.be/([^?&]+)",         # youtu.be/xxxx
        r"youtube\.com/shorts/([^?&]+)"  # youtube.com/shorts/xxxx
    ]
    for pattern in patterns:
        match = re.search(pattern, video_url)
        if match:
            return match.group(1)
    return ""

def get_transcript(video_url: str) -> str:
    try:
        video_id = get_video_id(video_url)
        if not video_id:
            return "Error: Invalid YouTube URL."

        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        transcript = None
        for t in transcript_list:
            if not t.is_generated:
                transcript = t
                break

        if transcript is None:
            for t in transcript_list:
                if t.is_generated:
                    transcript = t
                    break

        if transcript is None:
            return "Error: No transcript available in any language."

        transcript_text = " ".join([segment.text for segment in transcript.fetch()])
        return transcript_text

    except TranscriptsDisabled:
        return "Error: Transcripts are disabled for this video."
    except CouldNotRetrieveTranscript:
        return "Error: Could not retrieve the transcript."
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"
