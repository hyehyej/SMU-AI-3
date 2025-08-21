from io import BytesIO
import requests
from PIL import Image
from myllm.MyApi import geminiModel

def test(prompt, img):
    model = geminiModel()
    response = model.generate_content([prompt, img]) #두개가들어가면리스트[]
    print(response.text)

if __name__ =='__main__':
    image_url = "https://www.ccbk.co.kr/m/static/images/brand/img_04.png"  # 실제 이미지 URL로 교체
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt = "이 이미지에 있는 음료의 영양성분과 칼로리 같은 성분과 많이 먹었을 경우 부작용과 해로운 것을 알려줘 제로도!"
    test(prompt, img)