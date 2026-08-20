# views/vision.py
import streamlit as st

from services.vision_service import (
    describe_image
)

def show():
    st.title("👁️ Visão Computacional")
    image = st.file_uploader(
        "Selecione uma imagem",
        type=[
            # "png",
            "jpg",
            "jpeg"
        ]
    )

    if image:
        st.image(image)
        prompt = st.text_input("O que deseja analisar?")
        if st.button("analisar"):
            result = describe_image(
                image.getvalue(),
                prompt
            )
            st.markdown(result)