# views/live_talk.py
import hashlib

import streamlit as st

from config.settings import (
    LIVE_TALK_LANGUAGE,
    LLM_PROVIDER,
    STT_PROVIDER,
    TTS_PROVIDER,
)
from services.llm_service import chat
from services.stt_service import transcribe
from services.tts_service import synthesize


def show():
    st.title("🎙️ Conversa ao Vivo")
    st.caption(
        f"LLM: {LLM_PROVIDER} · STT: {STT_PROVIDER} · TTS: {TTS_PROVIDER}"
    )

    idiomas = {
        "pt-BR": "português do Brasil",
        "en-US": "inglês",
    }
    idioma = idiomas.get(LIVE_TALK_LANGUAGE, LIVE_TALK_LANGUAGE)

    if "live_messages" not in st.session_state:
        st.session_state.live_messages = [
            {
                "role": "system",
                "content": (
                    f"Você é um assistente de voz. Responda sempre em {idioma}, "
                    "de forma natural e objetiva, como numa conversa falada. "
                    "Evite respostas longas ou listas — fale como se estivesse "
                    "conversando."
                ),
            }
        ]
    if "live_last_audio_hash" not in st.session_state:
        st.session_state.live_last_audio_hash = None
    if "live_audio_bytes" not in st.session_state:
        st.session_state.live_audio_bytes = None
    if "live_audio_needs_play" not in st.session_state:
        st.session_state.live_audio_needs_play = False

    for message in st.session_state.live_messages:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.write(message["content"])

    _, col_limpar = st.columns([8, 1])
    with col_limpar:
        if st.button("🗑️", help="Limpar conversa", use_container_width=True):
            st.session_state.live_messages = [st.session_state.live_messages[0]]
            st.session_state.live_last_audio_hash = None
            st.session_state.live_audio_bytes = None
            st.session_state.live_audio_needs_play = False
            st.rerun()

    if st.session_state.live_audio_bytes:
        st.audio(
            st.session_state.live_audio_bytes,
            format="audio/mp3",
            autoplay=st.session_state.live_audio_needs_play,
        )
        st.session_state.live_audio_needs_play = False

    audio = st.audio_input("Toque para falar")
    if audio is None:
        return

    audio_bytes = audio.getvalue()
    audio_hash = hashlib.md5(audio_bytes).hexdigest()
    if audio_hash == st.session_state.live_last_audio_hash:
        return

    st.session_state.live_last_audio_hash = audio_hash
    with st.spinner("Ouvindo..."):
        texto = transcribe(audio_bytes)
    st.session_state.live_messages.append({"role": "user", "content": texto})

    with st.spinner("Pensando..."):
        resposta = chat(texto, st.session_state.live_messages)
    st.session_state.live_messages.append(
        {"role": "assistant", "content": resposta}
    )

    with st.spinner("Gerando voz..."):
        st.session_state.live_audio_bytes = synthesize(resposta)
    st.session_state.live_audio_needs_play = True
    st.rerun()