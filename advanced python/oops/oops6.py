class Person:
    def __init__(self, name, age):     # constructor
        self.name = name
        self.age = age

    def printVal(self):
        print("name:", self.name)
        print("age:", self.age)


obj = Person("anu", 25)
obj.printVal()