import streamlit as st

# Configuração da página
st.set_page_config(page_title="Acesso Privado", page_icon="🐈")

# Título centralizado
st.markdown("<h2 style='text-align: center;'>Área Restrita</h2>", unsafe_allow_html=True)

# 1. O GATO VOLTOU! (GIF Divertido e Centralizado)
col1, col2, col3 = st.columns([1, 4, 1]) # Cria colunas para centralizar
with col2:
    # Este é o link do novo GIF engraçado de um gato dando tchau
    st.image("https://media.giphy.com/media/VbnUQpnihTlgA/giphy.gif", use_column_width=True)

st.markdown("<p style='text-align: center;'>O gato está de olho... Digite a senha!</p>", unsafe_allow_html=True)

# 2. Entrada da Senha (A senha é 06022026)
senha = st.text_input("Insira o código de acesso:", type="password")

# 3. Verificação
if senha:
    if senha == "06022026":
        st.success("Acesso confirmado! Bem-vindo.")
        st.balloons() # Efeito de balões
        
        # Conteúdo que aparece após acertar a senha
        st.divider()
        st.markdown("### 🎉 Você entrou!")
        st.write("O gatinho te deu passagem. Este é o início do nosso projeto mobile.")
        st.info("O que vamos construir nesta área agora?")
        
    else:
        st.error("Senha incorreta. O gato não aprovou! 😿 Tente novamente.")
