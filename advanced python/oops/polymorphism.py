# poly - many  ;  morph - forms

# overloading not supported in python

# class Person:
#     def show(self, num1):
#         self.num1 = num1
#         print(self.num1)
#
#
# class Student(Person):
#     def show(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         print(self.num1, self.num2)
#
# obj = Student()
# obj.show(17, 25)
# # obj.show(5)      # this will show an error as overloading is not possible in python



# OVERRIDING -


class Person:
    def properties(self):
        print("10 Lakh RS, 2 Cars")

    def marry(self):
        print("with Ram")


class Child(Person):
    def marry(self):
        print("with Arun")


c = Child()
c.marry()
