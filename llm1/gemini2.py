from PIL import Image #일반적 이미지

from myllm.MyApi import geminiModel

def test():
    img = Image.open("img/owl.jpg")
    model = geminiModel()
    response = model.generate_content(["제시한 이미지를 3문장 이내의 한국어로 살명해 주세요",img])
    print(response.text)

if __name__ =='__main__':
    test()