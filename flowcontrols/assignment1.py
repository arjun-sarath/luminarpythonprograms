salary = int(input("enter salary: "))
yos = int(input("enter year of service: "))
if yos > 5:
    bonus = salary * (5/100)
    print("bonus: ", bonus)
else:
    print("no bonus")