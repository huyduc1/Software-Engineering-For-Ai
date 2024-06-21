from bson import ObjectId


def cast_to_string(id):
    if type(id) is not str:
        id = str(id)
    return id

def userEntity(item) -> dict:
    return {
        'id': str(item["_id"]),
        'name': item["name"],
        'age': item["age"],
        'email': item["email"],
        'password': item["password"],
        'gender': item["gender"]
    }

def usersEntity(items) -> list:
    return [userEntity(item) for item in items]

def serializeDict(user) -> dict:
    return {**{key: str(user[key]) for key in user if key == "_id"}, **{ key: user[key] for key in user if key != "_id"}}

def serializeList(users) -> list:
    return [serializeDict(user) for user in users]
