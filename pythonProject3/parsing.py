import json

data = {

    "firstName": "John",
    "email": "<john@mail.com",
    "salary": 25000,
    "age": 23,
    "human" : True

}

with open("data1.json", "w") as f:
    json.dump(data, f)