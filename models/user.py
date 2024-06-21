from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    password: str
    gender: str
    hashed_password: str
    disabled: bool
    role: str

class UserInDB(User):
    hashed_password: str
    