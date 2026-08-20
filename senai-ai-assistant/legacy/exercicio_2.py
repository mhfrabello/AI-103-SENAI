import streamlit as st
# Utilizar data
from datetime import datetime

# Logo
st.logo("./assets/senai_logo.jpg")
# Titulo 
st.title("SENAI AI Assistant")
# Obtendo a data/hora atual
hoje = datetime.now()
# Mostrando a data
st.write(hoje.strftime("%d/%m/%Y"))
# Utilizado a imagem
st.image("./assets/senai_logo.jpg",None,width=150)

nome = st.text_input("Seu nome")

perfil = st.selectbox(
    "Perfil",
    [
        "Aluno",
        "Professor",
        "Coordenador"
    ]
)

if st.button("Entrar"):
    st.success(
        f"Bem-vindo {nome}"
    )