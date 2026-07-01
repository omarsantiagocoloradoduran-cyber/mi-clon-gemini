import streamlit as st
from openai import OpenAI

# Configurar la página con el estilo de Isaac Newton
st.set_page_config(
    page_title="El Laboratorio de Newton",
    page_icon="🍎",
    layout="centered"
)

# --- ESTILO INTEGRADO (Tema Oscuro estilo Gemini / Newton) ---
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
        margin-top: 5%;
        margin-bottom: 1.5rem;
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
    /* Estilo para la caja de la clave */
    div[data-baseweb="input"] {
        background-color: #1e1f22 !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título temático de Newton
st.markdown('<h1 class="main-title">🍎 Hola, Omar, ¿qué ley de la naturaleza descubriremos hoy?</h1>', unsafe_allow_html=True)

# Entrada manual de la API Key (para que no falle nunca)
user_api_key = st.text_input("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", type="password")

# Entrada de texto para la consulta científica
prompt = st.text_area("", placeholder="Pregúntale algo a Newton...", key="input_box", height=70)

if st.button("Consultar a la IA"):
    if not user_api_key:
        st.error("Por favor, introduce tu API Key arriba para que Newton pueda responderte.")
    elif prompt:
        try:
            with st.spinner("Buscando en las leyes del universo..."):
                client = OpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=user_api_key
                )
                
                completion = client.chat.completions.create(
                    model="openrouter/auto", 
                    messages=[
                        {
                            "role": "system",
                            "content": "Eres Isaac Newton. Responde de forma sabia, científica pero amable, como si estuvieras en el siglo XVII descubriendo la gravedad."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                st.markdown("### 📜 Sabiduría de Newton:")
                st.write(completion.choices[0].message.content)
                
        except Exception as e:
            st.error(f"Error: Asegúrate de que tu clave es correcta. Detalle: {e}")
    else:
        st.warning("Escribe tu duda primero.")
