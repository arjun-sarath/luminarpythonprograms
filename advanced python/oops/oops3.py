class Employee:
    company_name = "LUMINAR TECHNOLOGIES"

    def __init__(self, name, ae, id, salary):    # constructor
        self.name = name
        self.ae = ae
        self.id = id
        self.salary = salary

    def printVal(self):
        print("company name:", Employee.company_name)
        print("employee name: ", self.name)
        print("employee age: ", self.ae)
        print("employee id: ", self.id)
        print("employee salary: ", self.salary)


obj = Employee("Arjun", 23, 2, 34000)
obj.printVal()


