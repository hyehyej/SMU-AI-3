import streamlit as st
from PIL import Image

from MyLLM import save_carpturefile, geminiModel, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 5")

# Page
st.title("Page 5")
picture = st.camera_input("Take a picture")

if picture:
    st.info("이미지를 캡쳐 했습니다.")
    save_carpturefile("capture", picture, "temp.png", st)
    text = st.text_area(label="질문입력:",  placeholder="질문을 입력 하세요")
    if st.button("SEND"):
        img = Image.open("capture/temp.png")
        model = geminiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response = model.generate_content( [ text , img ] )
        my_bar.empty()
        st.info(response.text)





'''
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
'''