import streamlit as st
from PIL import Image

st.set_page_config(page_title="✨ AI Чат-бот", layout="wide")

# Загрузка изображения
img = Image.open(r"D:\long.png")

# Создаём две колонки: для заголовка и изображения
col1, col2 = st.columns([3, 1])  # 3:1 — соотношение ширины

with col1:
    st.title("🤖ChatBot")  # Заголовок

with col2:
    st.image(img, width=200)






st.markdown("""
<style>
    
    
    .stApp {
        background: linear-gradient(135deg, #e6f2ff, #b3d9ff);
    }
    .stChatInput {
        position: fixed !important;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        max-width: 800px;
        z-index: 999;
    }
    
  
    
    .stChatMessage {
        margin-bottom: 70px; /* Чтобы сообщения не перекрывались полем ввода */
    }
</style>
""", unsafe_allow_html=True)
# Боковая панель
with st.sidebar:
    st.title("⚙️ Настройки")
    if st.button("Очистить историю"):
        st.session_state.messages = []




# История сообщений
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    avatar = "✋" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


if prompt := st.chat_input("Напишите сообщение..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="✋"):
        st.markdown(prompt)

    # Ответ бота (заглушка или LLM)
    bot_response = f"""
    **Ответ на ваш запрос:**  
    > *"{prompt}"*  

    Я пока что просто демо-бот, но скоро научусь отвечать умнее!  
    """
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_response)