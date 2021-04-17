# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages       # self.pages contain pages value of b1(1st argument in + statement and other.pages contain pages value of b2
#
#
# b1 = Book(100)
# b2 = Book(200)
# print(b1 + b2)





class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __sub__(self, other):
        return "overloading subtraction"

    def __mul__(self, other):
        return "overloading multiplication"

    def __truediv__(self, other):
        return "overloading true division"

    def __str__(self):
        return str(self.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
print(b1 + b2 + b3)
