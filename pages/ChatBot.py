import streamlit as st
from PIL import Image
import requests
import os

st.set_page_config(page_title="✨ AI Чат-бот", layout="wide")

# Загрузка изображения
img = Image.open(r"D:\long.png")

# Создаём две колонки: для заголовка и изображения
col1, col2 = st.columns([3, 1])  # 3:1 — соотношение ширины

with col1:
    st.title("🤖ChatBot")  # Заголовок

with col2:
    st.image(img, width=300)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e6f2ff, #b3d9ff);
    }

    /* Стили для сообщений пользователя */
    div[data-testid="stChatMessage"] {
        border: 2px solid #4da6ff;
        border-radius: 10px;
        padding: 12px;
        margin: 10px 0;
        background-color: rgba(255, 255, 255, 0.8);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    /* Стили для сообщений бота */
    div[data-testid="stChatMessage"]:has(> div:first-child > .st-emotion-cache-1kyxreq > div:contains('🤖')) {
        border: 2px solid #66b3ff;
        background-color: rgba(230, 242, 255, 0.9);
    }

    /* Стили для поля ввода */
    .stChatInput {
        position: fixed !important;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        max-width: 800px;
        z-index: 999;
        background: white;
        border-radius: 20px;
        padding: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    /* Аватарки */
    .st-emotion-cache-1kyxreq {
        margin-right: 10px !important;
    }
</style>
""", unsafe_allow_html=True)


def get_langflow_response(user_input):
    try:
        api_key = os.environ["LANGFLOW_API_KEY"]
    except KeyError:
        st.error("LANGFLOW_API_KEY environment variable not found. Please set your API key.")
        return None

    url = "http://localhost:7861/api/v1/run/e8a8daf6-34db-4e3b-b7b2-cd9f8e051f24"

    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": user_input
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("result", {}).get("response", "Не удалось получить ответ от API")
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка при запросе к API: {e}")
        return None


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Здравствуйте! Я ваш помощник по документации Tatlin Unified. Чем могу помочь?"}
    ]

# Отображение истории чата
for message in st.session_state.messages:
    avatar = "✋" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Обработка ввода пользователя
if prompt := st.chat_input("Задайте вопрос о Tatlin Unified..."):
    # Добавляем сообщение пользователя в историю
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="✋"):
        st.markdown(prompt)

    # Получаем ответ от API Langflow
    with st.spinner("🔍 Ищем ответ в документации..."):
        bot_response = get_langflow_response(prompt)

    # Если ответ получен, добавляем его в историю
    if bot_response:
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(bot_response)

# Боковая панель
with st.sidebar:
    st.title("⚙️ Настройки")
    if st.button("Очистить историю"):
        st.session_state.messages = []




