import streamlit as st
from openai import OpenAI

# Configuración de OpenRouter
# Reemplaza "TU_OPENROUTER_API_KEY" por tu clave real de OpenRouter (sk-or-...)
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
    if pregunta.strip():
        with st.spinner("Pensando tu respuesta... 🧠"):
            try:
                # Llamada limpia usando el modelo gratuito de Mistral
                completion = client.chat.completions.create(
                    model="mistralai/mistral-7b-instruct:free",
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
