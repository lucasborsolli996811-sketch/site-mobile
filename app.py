import streamlit as st

# Configuração da página para ficar romântica
st.set_page_config(page_title="Para Danielly ❤️", page_icon="💍")

# Inicializa o estado do acesso
if 'acesso_liberado' not in st.session_state:
    st.session_state.acesso_liberado = False

# --- TELA 1: O LOGIN DO GATINHO ---
if not st.session_state.acesso_liberado:
    st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)
    
    # O Gato dando tchau
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXAxbW1idGZ0ZzVqbmhxdm94bmhxbmhxbmhxbmhxbmhxbmhxbmhxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_container_width=True)
    
    st.markdown("<p style='text-align: center;'>Digite a senha para ver a surpresa!</p>", unsafe_allow_html=True)
    
    senha = st.text_input("Senha de acesso:", type="password")
    
    if senha == "06022026":
        st.session_state.acesso_liberado = True
        st.rerun()
    elif senha != "":
        st.error("Senha incorreta!")

# --- TELA 2: O PEDIDO ESPECIAL ---
else:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ Momento Especial ❤️</h1>", unsafe_allow_html=True)
    
    # Um GIF romântico ou fofo
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZqZW9pZGR4ZzR6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCAmY3Q9Zw/KztT2c4u8mYYUiMKdJ/giphy.gif", use_container_width=True)

    st.write("---")
    
    # A PERGUNTA
    st.markdown("<h3 style='text-align: center;'>Danielly Ferreira dos Santos,</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Você aceita namorar comigo?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM! ✅"):
            st.balloons()
            st.success("ELA DISSE SIM! O nosso futuro começa agora! 💍🌹")
            st.write("Dê um print nessa tela e me mande agora mesmo! ❤️")
            
    with col2:
        if st.button("NÃO... ❌"):
            st.warning("O sistema encontrou um erro: Esta opção é inválida! Tente o botão do lado. 😉")

    st.write("---")
    st.caption("Site criado com carinho através da Forja ⚒️")
