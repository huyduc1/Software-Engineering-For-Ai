from bson import ObjectId
def cast_to_string(id):
    if type(id) is not str:
        print("check")
        id = str(id)
    print("+++++++++++++")
    return id

def userEntity(item) -> dict:
    # if item["_id"] is None:
    #     print("id is none")
    print(type(item))
    # print(item["_id"])
    # print(type(item["_id"]))
    # print(type(item["_id"]) is str)
    return {
        
        'id': cast_to_string(item["_id"]),
        'name': item["name"],
        'age': item["age"],
        'email': item["email"],
        'password': item["password"],
        'gender': item["gender"]
    }

def usersEntity(items) -> list:
    return [userEntity(item) for item in items]



