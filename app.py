import streamlit as st

# Configuração da página
st.set_page_config(page_title="Para Danielly ❤️", page_icon="💍")

# Inicializa o estado de acesso
if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- PÁGINA 1: ENTRADA COM O GATO E DICA ---
if not st.session_state.logado:
    st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)
    
    # O Gato dando tchau
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXAxbW1idGZ0ZzVqbmhxdm94bmhxbmhxbmhxbmhxbmhxbmhxbmhxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_container_width=True)
    
    st.markdown("<p style='text-align: center;'>O gatinho está guardando uma surpresa!</p>", unsafe_allow_html=True)
    
    # Campo de senha
    senha = st.text_input("Digite o código para entrar:", type="password")
    
    # BOTÃO DE DICA
    if st.button("💡 Precisa de uma dica?"):
        st.info("Dica: É a data do nosso primeiro encontro! (DDMMAAAA)")

    # Verificação da senha (06022026)
    if senha == "06022026":
        st.session_state.logado = True
        st.rerun()
    elif senha != "":
        st.error("Senha incorreta! Tente lembrar da nossa data especial... ❤️")

# --- PÁGINA 2: O PEDIDO PARA DANIELLY ---
else:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ Momento Especial ❤️</h1>", unsafe_allow_html=True)
    
    # GIF romântico
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZqZW9pZGR4ZzR6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCAmY3Q9Zw/KztT2c4u8mYYUiMKdJ/giphy.gif", use_container_width=True)

    st.write("---")
    
    # O Pedido
    st.markdown("<h3 style='text-align: center;'>Danielly Ferreira dos Santos,</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Você aceita namorar comigo?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM! ✅"):
            st.balloons()
            st.success("ELA DISSE SIM! ❤️ Nosso futuro começa agora! 💍")
            st.write("Tira um print e me manda! Te amo!")
            
    with col2:
        if st.button("NÃO... ❌"):
            st.warning("Erro no sistema: Essa opção não está disponível para você! Escolha o outro botão. 😉")

    st.write("---")
    st.caption("Criado com amor via Forja ⚒️")
