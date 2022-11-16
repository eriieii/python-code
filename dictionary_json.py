users = {
    "id" : 1,
    "name" : "Leanner Graham",
    "username" : "graham",
    "email" : "graham@biz.com",
    "address" : {
        "street": "Jalan Kampung",
        "suite": "Kampung Rambutan",
        "city": "Bandung",
        "poscode": "40291",
        "wilayah": {
            "rt" : "04",
            "rw" : "02"
        }
    }
}

print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["wilayah"])
print(users["address"]["wilayah"]["rt"])

print("\nCara Import JSON")
import json
result = json.dumps(users)
print(result)

with open("result.json", "w") as file:
    json.dump(users, file)