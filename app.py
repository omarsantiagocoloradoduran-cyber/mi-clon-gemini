import streamlit as st
import requests

# 1. Configuración de la página web (Pestaña del navegador)
st.set_page_config(page_title="Mi Clon de Gemini", page_icon="🤖", layout="centered")

# Estilo personalizado para poner las burbujas de chat bonitas
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; padding: 10px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Mi Clon de Gemini en la Web")
st.caption("Una Inteligencia Artificial conectada a la nube, creada por Omar Santiago")

# 2. Tu API Key (Colócala aquí adentro)
API_KEY = "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"
URL = "https://openrouter.ai/api/v1/chat/completions"

# 3. Inicializar el historial de chat en la memoria de la página web
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres una IA idéntica a Gemini: auténtica, inteligente, empática y con un toque de ingenio. Hablas español a la perfección."}
    ]
    # ¡Aquí está tu saludo de bienvenida automático!
    st.session_state.bienvenida = "🤖 ¡Bienvenido! Estoy listo para responder tus dudas."

# Mostrar el saludo de bienvenida en la interfaz
st.chat_message("assistant").write(st.session_state.bienvenida)

# 4. Mostrar los mensajes anteriores del historial si existen
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# 5. Barra de texto para que el usuario escriba
if usuario_input := st.chat_input("Escribe tu pregunta aquí..."):
    
    # Mostrar el mensaje del usuario en la pantalla de inmediato
    st.chat_message("user").write(usuario_input)
    st.session_state.messages.append({"role": "user", "content": usuario_input})
    
    # Llamada a la API de OpenRouter
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openrouter/auto",
        "messages": st.session_state.messages
    }
    
    # Animación de "Pensando..." mientras llega la respuesta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                respuesta = requests.post(URL, json=payload, headers=headers, timeout=15)
                if respuesta.status_code == 200:
                    data = respuesta.json()
                    respuesta_ia = data["choices"][0]["message"]["content"]
                    
                    # Mostrar la respuesta en la web
                    st.write(respuesta_ia)
                    st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
                else:
                    st.error(f"Error del servidor (Código {respuesta.status_code})")
            except Exception as e:
                st.error(f"Error de conexión: {e}")