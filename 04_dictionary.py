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

# practice

#1. you are given a list of subjects, Assume one classroom is required for each subject. How many classrooms are needed by all students?

languages = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

# print(len(languages))

#2. write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.


marks = {}

# x = int(input("Enter physics : "))
# marks.update({"physics": x})
# x = int(input("Enter mathematics : "))
# marks.update({"mathematics": x})
# x = int(input("Enter chemistry : "))
# marks.update({"chemistry": x})

# print(marks)

#3. Figure out a way to store 9 & 9.0 as separate values in the set.
# values = 
values = {("float", 9.0), ("int", 9)}

print(values)