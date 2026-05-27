import streamlit as st
from streamlit import session_state

from functions import get_secret
from groq import Groq

api_key = get_secret("API_KEY")
client = Groq(api_key=api_key)
# No separate model object needed — just pass the model name directly in the request
model = "llama-3.3-70b-versatile"

temperature = st.sidebar.slider(
    label = "select temperature",
    min_value = 0.0,
    max_value = 2.0,
    value = 1.0,
)

st.set_page_config(page_title="AI Tutor", page_icon="🤖", layout="wide")
st.title("🤖 AI Programming Tutor")
st.caption("Powered by Groq & Llama 3")


if st.sidebar.button("Reset chat"):
    reset_chat()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if not st.session_state.chat_history:
    st.session_state.chat_history.append("Hii! How can i help you?")


user_message = st.chat_input("Type your message here")

if user_message:
    st.chat_message("user").write(user_message)
    st.session_state.chat_history.append(user_message)

    system_prompt = f"""
    You are a friendly and a programming tutor.
    Always explain concepts in a simple and clear way, using examples when possible.
    If the user asks something unrelated to programming, politely bring the conversation back to programming topics.
    """

    full_input = f"{system_prompt}\n\nUser Message\n\"\"\"{user_message}\"\"\""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": full_input}
        ],
        temperature=temperature,
        max_tokens=1000
    )
    assistant_reply = response.choices[0].message.content

    st.chat_message("assistant").write(assistant_reply)
    st.session_state.chat_history.append(("assistant", assistant_reply))



