import streamlit as st
from MyLLM import makeMsg, openAiModelArg, progressBar

st.sidebar.markdown("Clicked Page 7")

st.title("Page 7")

system = st.text_input("SYSTEM", placeholder="system을 입력")
text = st.text_input("질문을 입력", placeholder="질문을 입력")

if st.button("SEND"):
    if system and text:
        st.info(f"{system}에게 {text}문의 합니다.")##
        msg = makeMsg(system, text)

        my_bar = progressBar("Operation in progress. Please wait.") #모델 호출 전후에 넣어주기
        result = openAiModelArg("gpt-4o",msg)
        st.info(result)
    else:
        st.info("입력하세요")