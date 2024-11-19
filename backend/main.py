from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# FastAPI 인스턴스 생성
app = FastAPI()

# User 모델 정의
class User(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    email: str

# 사용자 데이터를 저장할 리스트 생성
users_db: List[User] = [
    User(id=1, name="Alice", age=30, email="alice@example.com"),
    User(id=2, name="Bob", age=25, email="bob@example.com"),
    User(id=3, name="Charlie", age=35, email="charlie@example.com")
]

# 전체 사용자 조회
@app.get("/users", response_model=List[User])
def get_users():
    return users_db

# 사용자 조회 by ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((user for user in users_db if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 사용자 추가
@app.post("/users", response_model=User)
def create_user(user: User):
    # ID 중복 체크
    if any(existing_user.id == user.id for existing_user in users_db):
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    users_db.append(user)
    return user

# 사용자 수정
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            users_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# 사용자 삭제
@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    for idx, user in enumerate(users_db):
        if user.id == user_id:
            deleted_user = users_db.pop(idx)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")

# 애플리케이션 실행 방법 (터미널에서 실행)
# uvicorn 파일명:app --reload
# 예: uvicorn main:app --reload
