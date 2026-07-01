import streamlit as st
from openai import OpenAI

# Configuración de OpenRouter
# Cambia "TU_OPENROUTER_API_KEY" por tu clave real (empieza por sk-or-...)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

st.set_page_config(page_title="Mi Clon de Gemini", page_icon="🤖")
st.title("🤖 Bienvenido")
st.write("Estoy aquí para responder tus dudas.")

# --- SECCIÓN DE TEXTO ---
pregunta = st.text_input("✍️ ¿En qué te ayudo hoy?", placeholder="Escribe tu pregunta o duda aquí...")

if st.button("Preguntar a la IA"):
    if pregunta.strip():  # Verifica que no esté vacío
        with st.spinner("Pensando tu respuesta... 🧠"):
            try:
                # Llamada a OpenRouter usando el modelo gratuito de Gemini 1.5 Flash
                completion = client.chat.completions.create(
                    model="google/gemini-flash-1.5", # Versión libre de Gemini en OpenRouter
                    messages=[
                        {
                            "role": "user",
                            "content": pregunta
                        }
                    ]
                )
                
                st.subheader("📝 Respuesta de la IA:")
                st.write(completion.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Hubo un error con OpenRouter: {e}")
    else:
        st.warning("Por favor, escribe una pregunta primero.")
