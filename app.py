import streamlit as st

# Configuração da página
st.set_page_config(page_title="Acesso Secreto", page_icon="🐈")

# Estilo para centralizar o layout no mobile
st.markdown("<h1 style='text-align: center;'>Bem-vindo!</h1>", unsafe_allow_html=True)

# 1. O Gato dando tchau (usando um GIF da internet)
# Se o link quebrar, você pode trocar por outro link de GIF de gato
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXJpZzR6eXNidGZ6cnR6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6bmZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCB3YXZpbmdfY2F0/3o72EX5QZ9N9d51dqo/giphy.gif", use_column_width=True)

st.markdown("<p style='text-align: center;'>Dê um tchauzinho de volta e digite a senha!</p>", unsafe_allow_html=True)

# 2. Campo de Senha
# O parâmetro type="password" faz os caracteres virarem bolinhas
senha = st.text_input("Digite a senha secreta:", type="password")

# 3. Lógica de entrada
if senha:
    if senha == "forja123": # Você pode escolher a senha que quiser aqui
        st.success("Acesso liberado!")
        st.balloons()
        
        # Aqui começa o conteúdo "secreto" do site
        st.write("---")
        st.subheader("Você entrou na área secreta da Forja ⚒️")
        st.write("Agora sim podemos começar a brincadeira!")
        
    else:
        st.error("Senha incorreta! O gato ficou triste. 😿")
