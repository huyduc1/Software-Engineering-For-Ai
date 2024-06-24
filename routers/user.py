from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity, serializeList, serializeDict
from bson import ObjectId

user = APIRouter()


"""

@user.get("/")
async def find_all_users():
    try:
        return usersEntity(conn.local.user.find())
    except Exception as e:
        return {"error": str(e)}    

@user.get("/{id}")
async def find_one_user(id):
    # print({"_id": ObjectId(id)})
    # print(conn.local.user.find_one({"_id": ObjectId(id)}))
    try:
        return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        return {"error": str(e)}

@user.post("/")
async def create_user(user: User):
    try:
        conn.local.user.insert_one(dict(user))
        return usersEntity(conn.local.user.find()) 
    except Exception as e:
        return {"error": str(e)}

@user.put("/{id}")
async def update_user(id, user: User):
    try:
        conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
        return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        return {"error": str(e)}

@user.delete("/{id}")
async def delete_user(id):
    try:
        return userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    except Exception as e:
        return {"error": str(e)}
"""


@user.get("/all-users")
async def find_all_users():
    try:
        return serializeList(conn.local.user.find())
    except Exception as e:
        return {"error": str(e)}    

@user.get("/{id}")
async def find_one_user(id):
    # print({"_id": ObjectId(id)})
    # print(conn.local.user.find_one({"_id": ObjectId(id)}))
    try:
        return serializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        return {"error": str(e)}

@user.post("/")
async def create_user(user: User):
    try:
        conn.local.user.insert_one(dict(user))
        return serializeList(conn.local.user.find()) 
    except Exception as e:
        return {"error": str(e)}

@user.put("/{id}")
async def update_user(id, user: User):
    try:
        conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
        return serializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))
    except Exception as e:
        return {"error": str(e)}

@user.delete("/{id}")
async def delete_user(id):
    try:
        return serializeDict(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    except Exception as e:
        return {"error": str(e)}