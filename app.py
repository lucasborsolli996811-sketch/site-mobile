import streamlit as st

# Configuração da página
st.set_page_config(page_title="Acesso Privado", page_icon="🐈")

# Título centralizado
st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)

# Centralizando o GIF com colunas para ficar bonito no celular
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    # Link novo e testado de um gatinho dando tchau
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXAxbW1idGZ0ZzVqbmhxdm94bmhxbmhxbmhxbmhxbmhxbmhxbmhxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_container_width=True)

st.markdown("<p style='text-align: center;'>Dê um tchauzinho de volta e digite a senha!</p>", unsafe_allow_html=True)

# Campo de senha (06022026)
senha = st.text_input("Senha de acesso:", type="password")

if senha:
    if senha == "06022026":
        st.success("Acesso confirmado!")
        st.balloons()
        st.divider()
        st.subheader("⚒️ Bem-vindo à Forja")
        st.write("Agora sim, com o gato devidamente posicionado, podemos seguir.")
    else:
        st.error("Senha incorreta! O gato não deixou você passar.")
