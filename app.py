import streamlit as st
from groq import Groq

# Configurar la página
st.set_page_config(
    page_title="Mi Asistente Escolar con IA",
    page_icon="✨",
    layout="centered"
)

# --- ESTILO INTEGRADO (Tema Oscuro estilo Gemini) ---
st.markdown("""
    <style>
    /* Fondo principal oscuro */
    .stApp {
        background-color: #0b0c10;
        color: #e5e5e5;
    }
    
    /* Centrar título */
    .main-title {
        text-align: center;
        font-family: 'Google Sans', sans-serif;
        font-size: 2.5rem;
        font-weight: 500;
        margin-top: 12%;
        margin-bottom: 2rem;
        color: #ffffff;
    }
    
    /* Caja de texto redondeada estilo barra de búsqueda de Gemini */
    div[data-baseweb="textarea"] {
        background-color: #1e1f22 !important;
        border: 1px solid #3c4043 !important;
        border-radius: 24px !important;
        padding: 5px 15px !important;
    }
    
    textarea {
        color: #ffffff !important;
    }

    /* Botón redondeado y minimalista */
    .stButton>button {
        background-color: #1e1f22;
        color: #c4c7c5;
        border: 1px solid #3c4043;
        border-radius: 20px;
        padding: 8px 24px;
        transition: all 0.3s;
        display: block;
        margin: 0 auto; /* Centrar el botón */
    }
    .stButton>button:hover {
        background-color: #2a2b2f;
        color: #ffffff;
        border-color: #a8c7fa;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar el cliente de Groq usando Secrets
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("Por favor, configura tu GROQ_API_KEY en los Secrets de Streamlit.")

# Título de la app centrado
st.markdown('<h1 class="main-title">Hola, Omar, ¿qué vamos a hacer hoy?</h1>', unsafe_allow_html=True)

# Cuadro de entrada de texto (Barra de búsqueda)
prompt = st.text_area("", placeholder="Pregunta a la IA...", key="input_box", height=70)

# Botón para preguntar
if st.button("Preguntar a la IA"):
    if prompt:
        try:
            with st.spinner("Pensando..."):
                # Petición de texto directa usando Llama 3
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="llama3-8b-8192",
                )
                
                # Mostrar la respuesta elegantemente
                st.markdown("### ✨ Respuesta:")
                st.write(chat_completion.choices[0].message.content)
                
        except Exception as e:
            st.error(f"Ocurrió un error al conectar con la IA: {e}")
    else:
        st.warning("Por favor, escribe una pregunta primero.")
