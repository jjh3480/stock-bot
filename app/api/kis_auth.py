import os

import requests
from dotenv import load_dotenv

# .env 파일 로드함
load_dotenv()

API_APP_KEY = os.getenv("KIS_APP_KEY")
API_APP_SECRET = os.getenv("KIS_APP_SECRET")

#모의투자 서버 토근 발급 URL
url="https://openapivts.koreainvestment.com:29443/oauth2/tokenP"

# HTTP 헤더 정보
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

# 요청 값
body = {
    "grant_type": "client_credentials",
    "appsecret": API_APP_SECRET,
    "appkey": API_APP_KEY
}

response = requests.post(
    url=url,
    json=body, # json 형태로 body 전송
    headers=headers
)

print(response.json())