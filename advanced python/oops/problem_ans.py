# class Student:
#     def __init__(self, name, roll, course, mark):
#         self.name = name
#         self.roll = roll
#         self.course = course
#         self.mark = mark
#
#     def printValue(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll)
#         print("Course:", self.course)
#         print("Mark:", self.mark)
#
#     def __str__(self):
#         return self.name
#
#
# f = open("problem", "r")
# for lines in f:
#     data = lines.rstrip("\n").split(",")
#     name = data[0]
#     roll = data[1]
#     course = data[2]
#     mark = data[3]
#     obj = Student(name, roll, course, mark)
#     if int(data[3]) > 190:
#         obj.printValue()
#         print("*" * 20)


# *******************************************************************************


class Student:
    def __init__(self, name, roll, course, mark):
        self.name = name
        self.roll = roll
        self.course = course
        self.mark = mark

    def printValue(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Course:", self.course)
        print("Mark:", self.mark)

    def __str__(self):
        return self.name


f = open("problem", "r")
obj = []
i = 0
max = 0
for lines in f:
    data = lines.rstrip("\n").split(",")
    name = data[0]
    roll = data[1]
    course = data[2]
    mark = data[3]
    obj.append(Student(name, roll, course, mark))
    # if int(data[3]) > 190:
    #     obj[i].printValue()
    #     print("*" * 20)
    # i += 1
    if int(data[3]) >= max:
        max = int(data[3])
    i += 1
for i in obj:
    if i.mark == max:
        i.printValue()