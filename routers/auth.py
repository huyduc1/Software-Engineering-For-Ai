from fastapi import APIRouter
from models.auth import User
from config.db import conn
from schemas.auth import *
from bson import ObjectId

auth = APIRouter()

@auth.post("/register")
async def register(email: str, pwd: str):
    try:
        user = dict(user)
        user["email"] = email
        conn.local.user.find_one({"email": str(email)})
    except Exception as e:
        return {"error": str(e)}