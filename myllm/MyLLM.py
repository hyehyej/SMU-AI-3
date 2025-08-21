from myllm.MyApi import geminiModel

def geminiMsg(msg):
    model = geminiModel()  # 어떤 버전의 모델 사용
    response = model.generate_content(msg)  # 질문
    return response.text
