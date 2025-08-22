import time

import streamlit as st
from click import prompt

from MyLLM import geminiTxt, progressBar

#번역기
#버튼을 눌렀을 때 해당 언어로 번역되는 페이지

st.sidebar.markdown("Clicked Page 4")

st.title("Page 4 transolate")

text = st.text_area(label="질문을 입력:", placeholder="질문을 입력하세요")

language = st.selectbox("언어를 선택 하세요", ["English", "Japanese", "Chinese"])

if st.button("SEND"):
    if text and language:
        st.write(f"선택된 옵션: {language}")
        st.info(text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = geminiTxt(f"{language}으로 다음 질문을 번역해줘{text}") #한번에 처리했음!!
        my_bar.empty()
        st.info(result)#화면 표시 창

    else:
        st.info("질문과 언어를 선택하세요")






'''
#입력 받기
user = st.text_area(label="입력",placeholder="입력하세요")

#언어 선택하기

selected_option = st.selectbox("언어을 선택하세요", ("Korean", "English", "Japanese", "German", "French"))
st.write(f"선택된 옵션: {selected_option}")

#출력 받기
if st.button("SEND"):
    if user and selected_option:
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------

        result = geminiTxt([user, selected_option])
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요")

'''