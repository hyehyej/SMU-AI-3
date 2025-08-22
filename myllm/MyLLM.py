from myllm.MyApi import geminiModel

def geminiMsg(msg):
    model = geminiModel()  # 어떤 버전의 모델 사용
    response = model.generate_content(msg)  # 질문
    return response.text

def openAiModel():
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

def makeMsg(system,user ):
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    return messages

def openAiModelArg(model, msgs):
    print(model)
    print(msgs)
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=msgs
    )
    return response.choices[0].message.content
