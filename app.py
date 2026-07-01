import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configura tu clave API de Gemini aquí
# (Recuerda usar tu propia API key)
genai.configure(api_key="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")

st.set_page_config(page_title="Mi Clon de Gemini 2.0", page_icon="🤖")
st.title("🤖 Mi Asistente Escolar con IA")
st.write("¡Sube una foto de tu tarea o escribe tu pregunta abajo!")

# --- SECCIÓN PARA SUBIR IMÁGENES ---
imagen_subida = st.file_uploader("📸 Sube una foto de tu tarea (opcional):", type=["jpg", "jpeg", "png"])

if imagen_subida:
    # Mostrar la imagen en la pantalla para que el usuario vea qué subió
    imagen = Image.open(imagen_subida)
    st.image(imagen, caption="Tarea cargada con éxito", use_container_width=True)

# --- SECCIÓN DE TEXTO ---
pregunta = st.text_input("✍️ ¿En qué te ayudo hoy con esta tarea?", placeholder="Ej: Explícame el problema de la foto paso a paso...")

if st.button("Pedir ayuda a la IA"):
    if pregunta or imagen_subida:
        with st.spinner("Analizando tu tarea... 🧠"):
            try:
                # Usamos el modelo más reciente que procesa texto e imágenes
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                # Armamos el contenido que le enviaremos a la IA
                contenido_a_enviar = []
                if imagen_subida:
                    contenido_a_enviar.append(imagen)
                if pregunta:
                    contenido_a_enviar.append(pregunta)
                else:
                    # Si sube foto pero no escribe nada, le damos una instrucción por defecto
                    contenido_a_enviar.append("Por favor, analiza esta imagen y ayúdame a resolverla o entenderla de forma educativa.")

                # Generamos la respuesta
                response = model.generate_content(contenido_a_enviar)
                
                st.subheader("📝 Explicación de la IA:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Hubo un error: {e}")
    else:
        st.warning("Por favor, escribe una pregunta o sube una foto primero.")