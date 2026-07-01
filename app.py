import streamlit as st
from openai import OpenAI

# Configurar la página
st.set_page_config(
    page_title="Mi Asistente Escolar con IA",
    page_icon="✨",
    layout="centered"
)

# --- ESTILO INTEGRADO (Tema Oscuro estilo Gemini) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0c10;
        color: #e5e5e5;
    }
    .main-title {
        text-align: center;
        font-family: 'Google Sans', sans-serif;
        font-size: 2.5rem;
        font-weight: 500;
        margin-top: 12%;
        margin-bottom: 2rem;
        color: #ffffff;
    }
    div[data-baseweb="textarea"] {
        background-color: #1e1f22 !important;
        border: 1px solid #3c4043 !important;
        border-radius: 24px !important;
        padding: 5px 15px !important;
    }
    textarea {
        color: #ffffff !important;
    }
    .stButton>button {
        background-color: #1e1f22;
        color: #c4c7c5;
        border: 1px solid #3c4043;
        border-radius: 20px;
        padding: 8px 24px;
        transition: all 0.3s;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover {
        background-color: #2a2b2f;
        color: #ffffff;
        border-color: #a8c7fa;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar cliente de OpenRouter de forma segura
client = None
if "OPENROUTER_API_KEY" in st.secrets:
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["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"]
        )
    except Exception as e:
        st.error(f"Error al inicializar el cliente: {e}")
else:
    st.error("Por favor, configura tu OPENROUTER_API_KEY en los Secrets de Streamlit.")

# Título de la app
st.markdown('<h1 class="main-title">Hola, Omar, ¿qué vamos a hacer hoy?</h1>', unsafe_allow_html=True)

# Entrada de texto
prompt = st.text_area("", placeholder="Pregunta a la IA...", key="input_box", height=70)

if st.button("Preguntar a la IA"):
    if not client:
        st.error("No se puede hacer la pregunta porque falta la configuración de la API Key en los Secrets.")
    elif prompt:
        try:
            with st.spinner("Pensando..."):
                completion = client.chat.completions.create(
                    model="openrouter/auto", 
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                st.markdown("### ✨ Respuesta:")
                st.write(completion.choices[0].message.content)
                
        except Exception as e:
            st.error(f"Ocurrió un error al conectar con OpenRouter: {e}")
    else:
        st.warning("Por favor, escribe una pregunta primero.")
