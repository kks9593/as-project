from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ✅ React 또는 외부에서 요청을 받을 수 있도록 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 프론트엔드 개발 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 데이터 모델 정의
class ASItem(BaseModel):
    id: int
    name: str
    content: str
    status: str = "접수됨"

# ✅ 임시 데이터베이스 (리스트)
db: List[ASItem] = []

# ✅ API 라우트 정의
@app.get("/as")
def get_as():
    return db

@app.post("/as")
def create_as(item: ASItem):
    db.append(item)
    return item
