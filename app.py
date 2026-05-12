import streamlit as st

# Configuração da página
st.set_page_config(page_title="Forja App", page_icon="⚒️")

# Inicializa o estado do acesso se não existir
if 'acesso_liberado' not in st.session_state:
    st.session_state.acesso_liberado = False

# --- PÁGINA 1: LOGIN COM O GATO ---
if not st.session_state.acesso_liberado:
    st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)
    
    # O Gato dando tchau (Link reforçado)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXAxbW1idGZ0ZzVqbmhxdm94bmhxbmhxbmhxbmhxbmhxbmhxbmhxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_container_width=True)
    
    st.markdown("<p style='text-align: center;'>Dê um tchauzinho e digite a senha!</p>", unsafe_allow_html=True)
    
    senha = st.text_input("Senha de acesso:", type="password")
    
    if senha == "06022026":
        st.session_state.acesso_liberado = True
        st.rerun() # Atualiza a página para entrar na fase 2
    elif senha != "":
        st.error("Senha incorreta! O gato não deixou passar.")

# --- PÁGINA 2: A PERGUNTA ---
else:
    st.markdown("<h2 style='text-align: center;'>⚒️ Segunda Fase</h2>", unsafe_allow_html=True)
    st.balloons()
    
    st.write("### ❓ Pergunta Importante:")
    resposta = st.radio(
        "Qual o seu próximo objetivo com a Forja?",
        ["Impressionar o mercado de Impressão 3D", 
         "Dominar os Desenhos Técnicos", 
         "Criar o site mais incrível do GitHub"]
    )
    
    if st.button("Confirmar Resposta"):
        st.success(f"Excelente escolha! Vamos focar em: {resposta}")
        st.info("Agora que você aprendeu a trocar de página, o que mais quer adicionar?")
        
    # Botão para voltar (opcional)
    if st.sidebar.button("Sair/Bloquear"):
        st.session_state.acesso_liberado = False
        st.rerun()
