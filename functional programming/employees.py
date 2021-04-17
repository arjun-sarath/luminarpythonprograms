class Employee:
    def __init__(this, eid, ename, desig, salary):
        this.eid = eid
        this.ename = ename
        this.desig = desig
        this.salary = salary

    def print_emp(self):
        print(self.ename)

f = open("employees")
employees = []
for lines in f:
    eid, ename, desig, salary = lines.rstrip("\n").split(",")
    e1 = Employee(eid, ename, desig, salary)
    employees.append(e1)
# sal = list(map(lambda emp:emp.salary, employees))
# highsal = max(sal)
# print(highsal)

developers = list(filter(lambda emp: emp.desig == "developer", employees))
print(developers)
