import streamlit as st
from PIL import Image
st.header("This is Dima header")
st.text("Mewmewmewmewmewmewmewmewmewmew")
st.subheader("This is Dima subheader")
st.write("Hello where are you from heheheheh")

if st.button("Click Me"):
    st.text("You pressed the button :)")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

user_input = st.text_input("Введите что-нибудь")
st.write(f"Вы ввели: {user_input}")
#if st.button("About"):
    #st.text("Welcome to our chatbot")


import streamlit as st
img = Image.open(r"D:\cat.jpg")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(img, width=200)
img2 = Image.open(r"D:\catt.jpg")
col11, col22, col33 = st.columns([1, 2, 1])
with col22:
    st.image(img2, width=200)
