import streamlit as st

# Configuração da página
st.set_page_config(page_title="Para Danielly ❤️", page_icon="💍")

# Estilo CSS para a animação da aliança giratória
st.markdown("""
    <style>
    @keyframes girar {
        from { transform: rotateY(0deg); }
        to { transform: rotateY(360deg); }
    }
    .alianca-container {
        display: flex;
        justify-content: center;
        align-items: center;
        perspective: 1000px;
        padding: 20px;
    }
    .alianca-girando {
        width: 250px;
        animation: girar 4s linear infinite;
        filter: drop-shadow(0 0 10px gold);
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializa o estado de acesso
if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- PÁGINA 1: ENTRADA ---
if not st.session_state.logado:
    st.markdown("<h2 style='text-align: center;'>🔒 Área Restrita</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXAxbW1idGZ0ZzVqbmhxdm94bmhxbmhxbmhxbmhxbmhxbmhxbmhxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihTlgA/giphy.gif", use_container_width=True)
    
    senha = st.text_input("Digite o código para entrar:", type="password")
    if st.button("💡 Precisa de uma dica?"):
        st.info("Dica: É a data do nosso primeiro encontro! (06022026)")

    if senha == "06022026":
        st.session_state.logado = True
        st.rerun()
    elif senha != "":
        st.error("Senha incorreta!")

# --- PÁGINA 2: O PEDIDO ---
else:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ Momento Especial ❤️</h1>", unsafe_allow_html=True)
    
    # Pergunta Principal
    st.markdown("<h3 style='text-align: center;'>Danielly Ferreira dos Santos,</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Você aceita namorar comigo?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Lógica do SIM
    with col1:
        if st.button("SIM! ✅"):
            st.session_state.resposta = "sim"
            
    # Lógica do NÃO
    with col2:
        if st.button("NÃO... ❌"):
            st.session_state.resposta = "nao"

    # --- RESULTADOS ---
    if 'resposta' in st.session_state:
        if st.session_state.resposta == "sim":
            st.balloons()
            # Aliança Gigante Girando
            st.markdown("""
                <div class="alianca-container">
                    <img class="alianca-girando" src="https://img.icons8.com/officel/480/diamond-ring.png">
                </div>
                <h2 style='text-align: center; color: gold;'>ELA DISSE SIM! ❤️💍</h2>
                """, unsafe_allow_html=True)
            st.success("O nosso futuro começa agora! Eu te amo!")

        elif st.session_state.resposta == "nao":
            st.snow()
            st.error("🚨 SISTEMA INVADIDO! OPÇÃO BLOQUEADA!")
            for _ in range(3): st.write("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
            
            st.markdown("### 📄 CONTRATO DE FINANCIAMENTO OBRIGATÓRIO")
            st.code("""
NOME: DANIELLY FERREIRA DOS SANTOS
CPF: 425.577.968-67
RG: 54.057.250-0
DATA NASCIMENTO: 21/01/2007

OBJETO: FINANCIAMENTO DO CIVIC 2020
VALOR TOTAL: R$ 110.000,00
PARCELAMENTO: 48x de R$ 4.230,00
            """, language="text")
            st.markdown("<h3 style='text-align: center; color: red;'>OPÇÃO DE NÃO SE TORNA UM FINANCIAMENTO OBRIGATÓRIO!</h3>", unsafe_allow_html=True)

    st.write("---")
    st.caption("Criado com amor via Forja ⚒️")
