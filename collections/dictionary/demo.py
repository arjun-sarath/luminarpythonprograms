# DICTIONARY


# definition

# dict1 = {}           # empty dictionary
# print(type(dict1))

# key-value pairs : used to add data/values to dictionary

# roll_no : 1001
# name : arun
# age : 25

# key : roll, name, age
#       1001, arun, 25

# student = {"roll_no": 1001, "name": "arun", "age": 25}
# print(student)


# supports heterogeneous values


# student1 = {"roll_no": 1001, "name": "arun", "age": 25, "age": 30}
# print(student1)                        # duplicate key not supported

# student1 = {"roll_no": 1001, "name": "arun", "age": 25, "cpp": 25}
# print(student1)                          # duplicate values supported


# insertion order preserved


student1 = {"roll_no": 1001, "name": "arun", "age": 25, "cpp": 25}
# print(student1["age"])               # values are fetched using its corresponding key
# print(student1["name"])

# for i in student1:
#     print(i, ":", student1[i])


# value modification/ updation

student1["name"] = "arjun"
student1["age"] = 30
student1["cpp"] += 10
print(student1)

# deleting key : using 'del' keyword

# del student1["cpp"]
# print(student1)

# adding new key and value

# print("total" in student1)              # checking whether key "total" is available in the dictionary
# print("cpp" in student1)

student1["total"] = 150                   # adding new key and values
print(student1)

