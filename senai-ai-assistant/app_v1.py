import streamlit as st
# Utilizar data
from datetime import datetime

# Obtendo a data/hora atual
hoje = datetime.now()

st.set_page_config(
    page_title="SENAI AI Assistant",
    page_icon="🤖"
)

metricas = [{"Descrição":"IA Ativas","Valor":150,"Variação":None},
            {"Descrição":"Documentos","Valor":45,"Variação":None},
            {"Descrição":"Usuários","Valor":38,"Variação":None},
            {"Descrição":"Consultas IA","Valor":123,"Variação":None},
            {"Descrição":"Documentos Analisados","Valor":432,"Variação":None},
            {"Descrição":"Agentes Criados","Valor":2,"Variação":None}
             ]

tabs = [{"Titulo": "Chat", "Conteudo": None},
        {"Titulo": "Documentos", "Conteudo": None},
        {"Titulo": "Sobre", "Conteudo": """Projeto desenvolvido
                                           durante o curso
                                           Desenvolvimento de Agentes com IA"""}]
      

st.title("SENAI AI Assistant")
# Canto superior esquerdo - Pequeno
st.logo("./assets/senai_logo.jpg")

# Menu Lateral

st.sidebar.write(f"""### **Matheus Rabello**  
**Usuário**  
{datetime.now().strftime("%d/%m/%Y %H:%M")}  
""")

st.sidebar.title("Menu")

opcoes = ["🏠 Início",
        "🤖 Chat IA",
        "📄 Documentos",
        "⚙ Configurações"]

opcao = st.sidebar.selectbox(
    "Escolha",opcoes   
)

# Conteiner com os indicadores

container = st.container()

with container:
    st.header("Dados")
    st.write("Informações")

for col, ele in zip(st.columns(len(metricas)), metricas):
    with col: st.metric(ele["Descrição"],ele["Valor"],ele["Variação"])


# Tabs 

for tab, ele in zip(st.tabs([it["Titulo"] for it in tabs]), tabs):
    with tab:
        if not ele["Conteudo"] == None:
            st.write(ele["Conteudo"])
        if ele["Titulo"]=="Documentos":
            documento = st.file_uploader(
        "Envie um arquivo"
            )

            if documento:
                st.success(
                "Arquivo enviado"
                )