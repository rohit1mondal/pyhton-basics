info = {
    "name" : "apnacollege",
    "subjects": ["python", "C", "java"],
    "topics": ("dictionary", "set"),
    "age": 24,
    "is_adult": True,
    45: 456.23
}
# print(info)

null_dict = {}
null_dict["name"] = "john"
# print(null_dict)

# nested dictionary

student = {
    "name": "Alice",
    "subjects": {
        "math":97,
        "physics": 70,
        "chemistry": 64
    }
}
# print(student["subjects"]["math"])

# methods
# print(info.keys())
# print(info.values())
# print(info.items())
# print(student["name"])
# print(student.get("name"))

new_info = {"city":"Kolkata"}
student.update(new_info)
# print(student)

# sets

collection = {1,2,3,4,4,4,"hello","world"}
# print(collection)

new_set = set() # empty set
new_set.add(5)
new_set.add(8)
new_set.add("hey")
new_set.add((1,2,3))

# print(new_set)

# new_set.remove(8)
# new_set.clear()

new_set.pop()
# print(new_set)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

# print(set1.union(set2))
# print(set1.intersection(set2))

# 