# 1.

# class College:
#     collegename = "LT"
#
#     def __init__(self, name, rollno):
#         self.roll = rollno
#         self.name = name
#
#     def printDetails(self):
#         print("college name:", self.collegename)
#         print("name of student:", self.name)
#         print("roll no:", self.roll)
#
#     def __str__(self):
#         return self.name + str(self.roll)        # __str__ is used to store any value in the object name variable
#
#
# ob = College("Anu", 4)
# print(ob)


# *************************************************

# 2.

class Employee:
    companyname = "Luminar Technolab"

    def __init__(self, name, id, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def printDetails(self):
        print("Company Name:", self.companyname)
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee salary:", self.salary)

    def __str__(self):
        return str(self.id)


emp = Employee("Arjun", 1007, 22, 25000)
print(emp)
# emp.printDetails()