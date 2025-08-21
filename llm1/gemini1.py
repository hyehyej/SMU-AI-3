from openai import chat, responses  # Assuming this is a valid import
from myllm.MyApi import geminiModel  # Your custom Gemini wrapper
import os
from openai.types import model


def test(txt):
    model = geminiModel()
    responses = chat.send_message(user_message)

    return(responses.text)

if __name__ =='__main__':

    chat = model.start_chat(history=[])

    while True:
        print("=== Gemini 챗봇 시작 ===")
        print("질문을 입력하세요")
        user_message = input("나: ")
        if user_message.lower() == '종료':
            break

        print("Gemini: ", responses.text)
    print("===챗봇 종료===")
    print(chat.history)