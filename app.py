import streamlit as st
import google.generativeai as genai

# Configura tu clave API de Gemini aquí
genai.configure(api_key="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")

st.set_page_config(page_title="Mi Clon de Gemini", page_icon="🤖")
st.title("🤖 Bienvenido")
st.write("Estoy aquí para responder tus dudas.")

# --- SECCIÓN DE TEXTO ---
pregunta = st.text_input("✍️ ¿En qué te ayudo hoy?", placeholder="Escribe tu pregunta o duda aquí...")

if st.button("Preguntar a la IA"):
    if pregunta.strip():  # Verifica que no esté vacío o solo con espacios
        with st.spinner("Pensando tu respuesta... 🧠"):
            try:
                # Usamos gemini-1.5-flash que es rápido y versátil
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Generamos la respuesta directamente con el texto
                response = model.generate_content(pregunta)
                
                st.subheader("📝 Respuesta de la IA:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Hubo un error al procesar con la IA: {e}")
    else:
        st.warning("Por favor, escribe una pregunta primero.")
