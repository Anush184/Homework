import json


people = {
    "name": "John",
    "surname": "Brown",
    "age": 37,
    "height": 82,
    "profession": "programmer",
    "eyes color": "blue",
    "hobbes": {
        "sport": True,
        "reading": False,
        "music": True,
        "dancing": False,
        "travel": True
    },
    "phone_number": None,
    "home address": None,
    "has animal": False
}
json_obj = json.dumps(people, indent=2)

with open("output_json.txt", "w") as f:
    f.write(json_obj)
