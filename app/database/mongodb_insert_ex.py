from pymongo import MongoClient

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")

# 테이블
db = client["stock"]

# 테이블 내 패키지 생성
collection = db["test"]

# 데이터
data = {
    "name" : "삼성전자",
    "price" : 290000
}

# db에 저장
collection.insert_one(data)

print("MongoDB insert soccess")