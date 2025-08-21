from http.client import responses
from myllm.MyApi import openAiModel, openAiModelArg, makeMsg


def test():
    responses = openAiModelArg("gpt-4o", makeMsg("한국 선생님","서울의 맛집 알려줘"))
    print(responses)

if __name__ == '__main__':
    test()