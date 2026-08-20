# app.py
import streamlit as st
# importando biblioteca de tratamento de datas
from datetime import datetime
from views import dashboard, chat, rag, ocr, settings

st.set_page_config(
    page_title="SENAI AI Assistant",
    page_icon="./assets/senai_logo.jpg",
)
# Definições
menu = {
    1: {"titulo":"🏠 Dashboard", "pagina": dashboard.show },
    2: {"titulo":"🤖 IA Generativa","pagina": chat.show},
    3: {"titulo":"📄 RAG","pagina": rag.show},
    4: {"titulo":"📋OCR","pagina": ocr.show},
    5: {"titulo":"👁️Visão","pagina": None},
    6: {"titulo":"🕵️‍♂️Agentes","pagina": None},
    7: {"titulo":"⚙ Configurações","pagina": settings.show},
}
st.logo("./assets/senai_logo.jpg")
# Menu Lateral
st.sidebar.write(f"""**Rabello**  
**Usuário**  
{datetime.now().strftime("%d/%m/%Y %H:%M")}
""")
# Ajuste para deixar dinâmico o menu. Usamos uma função lambda
opcao = st.sidebar.selectbox("Menu Lateral",
        options=menu.keys(),
        format_func=lambda x: menu[x]["titulo"],
        index=0
    )
# Aqui chamamos a página se existir
if not menu[opcao]["pagina"] == None: menu[opcao]["pagina"]()