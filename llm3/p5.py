import os
import time

import streamlit as st

from MyLLM import geminiTxt, geminiModel
from PIL import Image

st.sidebar.markdown("Clicked Page 5")

st.title("Page 5")


def save_uploadedfile(directory, file):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 파일 저장 (이름 변경 없이 저장)
    with open(os.path.join(directory, picture.name), 'wb') as f:
        f.write(picture.getbuffer())
    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {picture.name} 저장되었습니다.')



picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

if picture:
    st.image(picture)
    save_uploadedfile("img", picture)

    text = st.text_area(label="질문입력:",
                        placeholder="질문을 입력 하세요")
    if st.button("SEND"):
        img = Image.open("img/"+picture.name)
        model = geminiModel()
        response = model.generate_content( [ text , img ] )
        st.info(response.text)