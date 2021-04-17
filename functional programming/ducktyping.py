class Swift:
    def start(self):
        print("swift car start method")

    def accelerate(self):
        print("swift car accelerate method")

    def brake(self):
        print("swift car brake method")


class Innova:
    def start(self):
        print("innova car start method")

    def accelerate(self):
        print("innova car accelerate method")

    def brake(self):
        print("innova car brake method")


class Person:
    def drive(self, car):
        car.start()
        car.accelerate()
        car.brake()

sw = Swift()
inno = Innova()
p = Person()
# p.drive(sw)
p.drive(inno)