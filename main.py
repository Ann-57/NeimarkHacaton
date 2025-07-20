import streamlit as st
from PIL import Image

# Настройка страницы
st.set_page_config(page_title="Tatlin Unified Документация 2.0", layout="wide")

# Стили
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e6f2ff, #b3d9ff);
    }
    .welcome-card {
        background-color: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .feature-card {
        background-color: rgba(255,255,255,0.8);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #4da6ff;
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
</style>
""", unsafe_allow_html=True)

# Логотип и заголовок (раскомментируйте если есть логотип)
img = Image.open(r"D:\logo.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
     st.image(img, width=200)

st.title("💬 Tatlin Unified Документация 2.0")
st.markdown("""
<div class="welcome-card">
    <h3 style="color: #1e3d8f;">Добро пожаловать в помощник по документации Tatlin Unified!</h3>
    <p>Этот AI-ассистент поможет вам быстро найти ответы в документации системы хранения данных.</p>
</div>
""", unsafe_allow_html=True)

# Блок "Как пользоваться" с белой рамочкой
with st.expander(" ", expanded=True):  # Пустой заголовок, так как мы добавим свой
    st.markdown("""
    <div style="
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    ">
        <h3 style="
            color: #1e3d8f;
            font-size: 1.4rem;
            margin-top: 0;
            margin-bottom: 15px;
        ">📌 Как пользоваться чат-ботом</h3>
        <ul style="margin-bottom: 0; padding-left: 20px;">
            <li style="margin-bottom: 10px; font-size: 1.1rem;"><strong>Задавайте вопросы</strong> о системе Tatlin Unified</li>
            <li style="margin-bottom: 10px; font-size: 1.1rem;"><strong>Получайте точные ответы</strong> основанные на соответствующих разделах документации</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Блок "Возможности"
st.subheader("🛠️ Возможности помощника")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🔍 Поиск в документации</h4>
        <p>Мгновенный поиск по всей базе документации Tatlin Unified</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h4>📚 Понятные ответы</h4>
        <p>Объяснение доступным языком сложных технических вопросов по Tatlin Unified</p>
        
    </div>
    """, unsafe_allow_html=True)






