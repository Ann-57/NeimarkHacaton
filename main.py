import streamlit as st
from PIL import Image
#img = Image.open(r"D:\logo.png")
#col1, col2, col3 = st.columns([1, 2, 1])
#with col2:
#    st.image(img, width=200)
st.title("💬ChatbotYADRO")
st.text("Данный чатбот создан для помощи с документацией системы хранения данных Tatlin Unified")

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





if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Как я могу помочь вам?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Напишите сообщение..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Ответ бота (заглушка или LLM)
    bot_response = f"""
    🚀 **Ответ на ваш запрос:**  
    > *"{prompt}"*  

    Я пока что просто демо-бот, но скоро научусь отвечать умнее!  
    """
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_response)
