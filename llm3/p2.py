import os
import streamlit as st
from PIL.Image import Image

##
st.title("Page 2")
# 선택한 파일을 저장하는 함수
def save_uploadedfile(directory, file):
    # 1. 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 파일 저장 (이름 변경 없이 저장)
    #st.info(file.name.split('.'))

    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())


    # 3. 저장 완료 메시지 출력
    st.success(f'저장 완료: {directory}에 {file.name} 저장되었습니다.')
##
st.sidebar.markdown("Clicked Page 2")

st.title("Page 2 Image Upload")
file = st.file_uploader('이미지 파일 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
if file:
    st.image(file)
    save_uploadedfile("img", file)
    
    
#사용자가 사진 선택시 사진이 서버로 전송
