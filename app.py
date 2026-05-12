import streamlit as st

# Configuração da página para parecer um App
st.set_page_config(page_title="Forja App", page_icon="⚒️")

# Título centralizado
st.markdown("<h2 style='text-align: center;'>⚒️ Acesso Restrito</h2>", unsafe_allow_html=True)

# Centralizando o GIF do gato dando tchau
# Se o GIF sumir de novo, o Streamlit apenas não mostrará nada, mas o site continua funcionando
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2ZueXNueXNueXNueXNueXNueXNueXNueXNueXNueXNueXNueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_column_width=True)

st.markdown("<p style='text-align: center;'>Dê um tchauzinho de volta e digite a senha!</p>", unsafe_allow_html=True)

# Campo de entrada da senha (A senha é 06022026)
senha = st.text_input("Qual é o segredo?", type="password")

if senha:
    if senha == "06022026":
        st.success("Acesso Liberado!")
        st.balloons()
        
        # Conteúdo que aparece após a senha correta
        st.divider()
        st.subheader("Bem-vindo à área de testes!")
        st.write("Agora o site está rodando com a senha que você escolheu.")
    else:
        st.error("Senha incorreta! Tente de novo.")
