import streamlit as st

# Configuração da página para celular
st.set_page_config(page_title="Acesso Secreto", page_icon="🐈")

# Título do site
st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)

# --- O GATO QUE VOCÊ QUERIA ESTÁ AQUI ABAIXO ---
# Usei um GIF de um gato dando tchau bem engraçado
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2ZueXNueXNueXNueXNueXNueXNueXNueXNueXNueXNueXNueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif")

st.markdown("<p style='text-align: center;'>Dê um tchauzinho de volta e digite a senha!</p>", unsafe_allow_html=True)

# Campo de senha
senha = st.text_input("Senha de acesso:", type="password")

# Lógica da senha que você definiu
if senha:
    if senha == "06022026":
        st.success("Acesso Liberado! O gato deixou você passar.")
        st.balloons()
        
        # Conteúdo após a senha
        st.divider()
        st.subheader("BEM-VINDO À FORJA ⚒️")
        st.write("Agora que o gatinho te deixou entrar, qual o próximo passo do nosso site?")
    else:
        st.error("Senha errada! O gato bloqueou sua entrada. 😾")
