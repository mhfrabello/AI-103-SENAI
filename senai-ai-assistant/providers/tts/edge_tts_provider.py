# providers/tts/edge_tts_provider.py
import asyncio

import edge_tts

from config.settings import EDGE_TTS_VOICE
from services.settings_service import load_settings

settings = load_settings()


async def _stream_audio(text: str) -> bytes:
    communicate = edge_tts.Communicate(
        text,
        settings.get("EDGE_TTS_VOICE", EDGE_TTS_VOICE),
    )
    audio = bytearray()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio.extend(chunk["data"])
    return bytes(audio)


def synthesize(text: str) -> bytes:
    return asyncio.run(_stream_audio(text))