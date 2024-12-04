import streamlit as st

# CSS para personalizar o tema e destaque da resposta
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1479142506502-19b3a3b7ff33?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
    }
    h1 {
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
    .stMarkdown p { 
        color: #D3D3D3;
    }
    .response-box {
        background-color: rgba(0, 0, 0, 0.8);
        color: #FFD700;
        font-size: 1.5rem;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #FFD700;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Assistente Jurídico")

st.markdown('Digite sua dúvida sobre Direito abaixo:', unsafe_allow_html=True)
user_input = st.text_input("Pergunte aqui:")

if st.button("Enviar"):
    if user_input.strip():
        st.markdown(
            f'<div class="response-box">Resposta: {user_input}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning("Por favor, digite algo antes de enviar.")
