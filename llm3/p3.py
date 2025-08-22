import time

import streamlit as st
from MyLLM import geminiTxt, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 3")

# Page
st.title("Page 3 프로그램 작성기")
text = st.text_area(label="질문을 입력:",
                    placeholder="질문을 입력 하세요")
selected_option = st.radio("언어를 선택하세요", ("java", "python", "c++"))

if st.button("SEND"):
    if text  and selected_option:
        st.write(f"선택된 옵션: {selected_option}")
        st.info(text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = geminiTxt(f" {selected_option}로 다음 질문을 코딩 해줘 {text}")
        my_bar.empty()
        st.code(result, language=selected_option)
    else:
        st.info(" 질문과 언어를 선택하세요")




#처음부터흐름제어하기! (흐름 파악하기)



'''
user = st.text_area(placeholder="입력", label="질문입력")

selected_option = st.radio("옵션을 선택하세요", ("C언어", "Python", "Java"))
st.write(f"선택된 옵션: {selected_option}")

if st.button("SEND"):
    if user:
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



