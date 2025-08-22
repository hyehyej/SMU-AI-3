import time

import streamlit as st

from MyLLM import geminiTxt, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 1")

# Page
st.title("Page 1")
text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
if st.button("SEND"):
    if text:
        st.info(text)
    else:
        st.info("질문을 입력 하세요")