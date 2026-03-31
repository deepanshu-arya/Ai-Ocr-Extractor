from fastapi import Depends, HTTPException
from jose import jwt
from datetime import datetime, timedelta

SECRET = "SECRET123"

def create_token(data: dict):
    return jwt.encode(data, SECRET, algorithm="HS256")

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")