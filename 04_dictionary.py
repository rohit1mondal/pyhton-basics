info = {
    "name" : "apnacollege",
    "subjects": ["python", "C", "java"],
    "topics": ("dictionary", "set"),
    "age": 24,
    "is_adult": True,
    45: 456.23
}
print(info)

null_dict = {}
null_dict["name"] = "john"
print(null_dict)

# nested dictionary

student = {
    "name": "Alice",
    "subjects": {
        "math":97,
        "physics": 70,
        "chemistry": 64
    }
}
print(student["subjects"]["math"])

# methods
print(info.keys())
print(info.values())
print(info.items())
print(student["name"])
print(student.get("name"))

new_info = {"city":"Kolkata"}
student.update(new_info)
print(student)