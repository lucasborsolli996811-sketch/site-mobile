import streamlit as st

# Configuração da página - Tema romântico
st.set_page_config(page_title="Para Danielly ❤️", page_icon="💍")

# Inicializa a memória do site para saber se ela já logou
if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- PÁGINA 1: ENTRADA COM O GATO E SENHA ---
if not st.session_state.logado:
    st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)
    
    # O Gato de comédia dando tchau (centralizado)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXAxbW1idGZ0ZzVqbmhxdm94bmhxbmhxbmhxbmhxbmhxbmhxbmhxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_container_width=True)
    
    st.markdown("<p style='text-align: center;'>Opa! Digite a senha para o gato te dar passagem:</p>", unsafe_allow_html=True)
    
    # A senha que você escolheu: 06022026
    senha = st.text_input("Senha de acesso:", type="password")
    
    if senha == "06022026":
        st.session_state.logado = True
        st.rerun() # Isso limpa a tela do gato e pula para o pedido
    elif senha != "":
        st.error("Senha incorreta! O gato não deixou você passar. 😾")

# --- PÁGINA 2: O PEDIDO PARA DANIELLY ---
else:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ Momento Especial ❤️</h1>", unsafe_allow_html=True)
    
    # GIF fofo de pedido/amor
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZqZW9pZGR4ZzR6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCAmY3Q9Zw/KztT2c4u8mYYUiMKdJ/giphy.gif", use_container_width=True)

    st.write("---")
    
    # O Pedido com o nome completo
    st.markdown("<h3 style='text-align: center;'>Danielly Ferreira dos Santos,</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Você aceita namorar comigo?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM! ✅"):
            st.balloons() # Chuva de balões na tela
            st.success("ELA DISSE SIM! ❤️ O nosso futuro começa agora! 💍")
            st.write("Dê um print e me mande! Eu te amo!")
            
    with col2:
        if st.button("NÃO... ❌"):
            st.warning("Ops! O botão de 'Não' está com defeito técnico... tente o outro! 😉")

    st.write("---")
    st.caption("Site personalizado criado via Forja ⚒️")
