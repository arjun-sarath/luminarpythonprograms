# SINGLE LEVEL INHERITANCE

# 1.

# class Parent:
#     parent_name = "Arun"
#
#     def m1(self, age):
#         self.age = age
#         print("parent name is", Parent.parent_name)
#         print("Parent age is", self.age)
#
#
# class Mobile:
#     def mob(self):
#         print("I have Samsung M21")
#
#
# class Child(Parent, Mobile):
#     def m2(self, c_age):
#         self.c_age = c_age
#         print("Parent name is", Parent.parent_name)
#         print("child age is", self.c_age)
#         print("parent age is", self.age)
#
#
# c = Child()
# c.m1(35)
# print("*"*50)           # just to seperate to classes in output
# c.m2(13)
# c.mob()

# 2.

# class Teacher:
#     teacher_name = "Lakshmi"
#
#     def m1(self, subject):
#         self.subject = subject
#         print("teacher name :", Teacher.teacher_name)
#         print("subject name :", self.subject)
#
#
# class Student(Teacher):
#     def m2(self, stud_name):
#         self.stud_name = stud_name
#         print("student name :", self.stud_name)
#         print("teacher name :", Teacher.teacher_name)
#         print("subject name :", self.subject)
#
#
# obj = Student()
# obj.m1("Mathematics")
# print("*"*50)
# obj.m2("Arun")

# ********************************************************************

# MULTIPLE INHERITANCE

# 1.

# class Parent:
#     parent_name = "Arun"
#
#     def m1(self, age):
#         self.age = age
#         print("parent name is", Parent.parent_name)
#         print("Parent age is", self.age)
#
#
# class Mobile:
#     def mob(self):
#         print("I have Samsung M21")
#
#
# class Child(Parent, Mobile):
#     def m2(self, c_age):
#         self.c_age = c_age
#         print("Parent name is", Parent.parent_name)
#         print("child age is", self.c_age)
#         print("parent age is", self.age)
#
#
# c = Child()
# c.m1(35)
# print("*"*50)           # just to seperate the classes in output
# c.m2(13)
# c.mob()


# MULTI LEVEL INHERITANCE

# 1.
#
# class Parent:
#     def m1(self):
#         print("inside parent")
#
#
# class Child(Parent):
#     def m2(self):
#         print("inside child")
#
#
# class Subchild(Child):
#     def m3(self):
#         print("inside sub-child")
#
#
# obj = Subchild()
# obj.m1()
# print("*"*50)
# obj.m2()
# print("*"*50)
# obj.m3()

# 2.

class Family:
    def show_family(self):
        print("This is our family:")


# Father class inherited from Family
class Father(Family):

    def show_father(self):
        self.fathername = "Mark"


# Mother class inherited from Family
class Mother(Family):

    def show_mother(self):
        self.mothername = "Sonia"


# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()  # Object of Son class
s1.show_father()
s1.show_mother()
s1.show_family()
s1.show_parent()

