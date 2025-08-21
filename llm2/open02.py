from myllm.MyApi import openAiModelArg, makeMsg


def test(prompt):
    modelName = "gpt-4o"
    msg = makeMsg("한문장으로 요약해줘", prompt)
    result = openAiModelArg(modelName, msg)#모델명, 메세지
    print(result)


if __name__ =='__main__':
   prompt = "SK하이닉스에 대해서 알려줘"
   test(prompt)