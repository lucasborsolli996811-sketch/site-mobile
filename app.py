import streamlit as st

# Configuração da página
st.set_page_config(page_title="Acesso Privado", page_icon="🐈")

# Título centralizado
st.markdown("<h2 style='text-align: center;'>Área Restrita</h2>", unsafe_allow_html=True)

# 1. O Gato dando tchau (GIF Centralizado)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    # GIF de um gatinho fofo dando tchau
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_column_width=True)

st.markdown("<p style='text-align: center;'>O gato só deixa passar quem tem a senha!</p>", unsafe_allow_html=True)

# 2. Entrada da Senha (A senha agora é 06022026)
senha = st.text_input("Insira o código de acesso:", type="password")

# 3. Verificação
if senha:
    if senha == "06022026":
        st.success("Acesso confirmado! Bem-vindo.")
        st.balloons()
        
        # Conteúdo que aparece após acertar a senha
        st.divider()
        st.markdown("### 🎉 Você entrou!")
        st.write("Este é o início do nosso projeto mobile.")
        st.info("O que vamos construir nesta área agora?")
        
    else:
        st.error("Senha incorreta. Tente novamente!")
