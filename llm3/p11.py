import streamlit as st
from PIL import Image

from MyLLM import makeImage, progressBar

st.sidebar.markdown("Clicked Page 11")

st.title("Page 11")

#이미지를 생성하고
#생성한 이미지의 클론을 만들기

text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")

name = st.text_area(label="이미지 이름:",
                    placeholder="이미지 이름을 입력 하세요")

if st.button("SEND"):
    if text and name:
        st.info(text)  # 텍스트 출력
        my_bar = progressBar("Operation in progress. Please wait.")
        makeImage(text, name)  # 이미지 받아옴?
        my_bar.empty()
        with open("img/"+name, "rb") as file:
            st.download_button(
                label = "Download image",
                data = file,
                file_name = "img/"+name,
                mime = "image/png"
            )
        img = Image.open("img/"+name)
        st.image(img)
    else:
        st.info("다시 입력하세요")