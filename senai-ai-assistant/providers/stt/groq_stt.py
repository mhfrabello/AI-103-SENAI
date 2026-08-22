# providers/stt/groq_stt.py
import groq

from config.settings import GROQ_API_KEY, GROQ_STT_MODEL, LIVE_TALK_LANGUAGE
from services.settings_service import load_settings

settings = load_settings()
client = groq.Groq(api_key=settings.get("GROQ_API_KEY", GROQ_API_KEY))


def transcribe(audio_bytes: bytes) -> str:
    response = client.audio.transcriptions.create(
        file=("audio.wav", audio_bytes),
        model=settings.get("GROQ_STT_MODEL", GROQ_STT_MODEL),
        language=settings.get("LIVE_TALK_LANGUAGE", LIVE_TALK_LANGUAGE)[:2].lower(),
        temperature=0.0,
    )
    return response.text