# addition program using class

class Addition:
    def find_sum(self, a, b):
        self.a = a
        self.b = b
        print("sum : ", self.a + self.b)


obj = Addition()

obj.find_sum(2, 6)

obj.find_sum(9, 8)
