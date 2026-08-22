# services/tts_service.py
from services.settings_service import load_settings


def synthesize(text: str) -> bytes:
    settings = load_settings()
    provider = settings.get("TTS_PROVIDER", "edge")

    if provider == "edge":
        from providers.tts.edge_tts_provider import synthesize
        return synthesize(text)
    return b""