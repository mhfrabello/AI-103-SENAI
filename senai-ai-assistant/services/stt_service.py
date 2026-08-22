# services/stt_service.py
from services.settings_service import load_settings


def transcribe(audio_bytes: bytes) -> str:
    settings = load_settings()
    provider = settings.get("STT_PROVIDER", "groq")

    if provider == "groq":
        from providers.stt.groq_stt import transcribe
        return transcribe(audio_bytes)
    return "Provider não configurado."