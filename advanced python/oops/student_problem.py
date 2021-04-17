# METHOD 1:
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def printValue(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
#
# f = open("student", "r")
# obj = []                                     # here object is taken as a list
# for lines in f:
#     words = lines.rstrip("\n").split(",")
#     obj.append(Student(words[0], words[1]))
# for i in obj:
#     i.printValue()
#     print("*"*50)




# METHOD 2

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printValue(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __str__(self):
        return self.name


f = open("student", "r")
obj = []
for lines in f:
    data = lines.rstrip("\n").split(",")
    name = data[0]
    age = data[1]
    obj = Student(name, age)
    print(obj)
    obj.printValue()
