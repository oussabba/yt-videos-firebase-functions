from firebase_functions import https_fn
from firebase_admin import initialize_app
from youtube_transcript_api import YouTubeTranscriptApi

initialize_app()

@https_fn.on_call()
def getTranscript(req: https_fn.CallableRequest):
    videoId = req.data["videoId"]
    languages = req.data["languages"]
    return YouTubeTranscriptApi.get_transcript(videoId,languages=languages)

@https_fn.on_call()
def translateTranscript(req: https_fn.CallableRequest):
    videoId = req.data["videoId"]
    fromLanguage = req.data["fromLanguage"]
    toLanguage = req.data["toLanguage"]
    transcript_list = YouTubeTranscriptApi.list_transcripts(videoId)
    transcript = transcript_list.find_transcript(fromLanguage)
    translated_transcript = transcript.translate(toLanguage)
    return translated_transcript.fetch()