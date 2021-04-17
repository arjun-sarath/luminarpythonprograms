# class      : design pattern
# object     : real world entity
# reference  : name that refers a memory location of an object

class Person:  # classname should start with a capital letter
    def walk(self):
        print("person is walking")

    def run(self):
        print("person is running")

    def jump(self):
        print("person is jumping")


obj = Person()
obj.walk()
obj.run()
obj.jump()

ab = Person()
ab.walk()

