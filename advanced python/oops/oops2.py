class Person:
    def setVal(self, name, age):
        self.age = age
        self.name = name

    def printVal(self):
        print("name: ", self.name)
        print("age: ", self.age)


obj = Person()
obj.setVal("ram", 23)
obj.printVal()