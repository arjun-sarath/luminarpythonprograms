age = int(input("enter age: "))
sex = input(" enter sex: ")
marstatus = input("enter marital status: ")
if sex == 'F':
    print("work in urban areas")
else:
    if (age > 20) & (age < 40):
        print("work anywhere")
    elif (age > 40) & (age < 60):
        print("work in urban areas")
    else:
        print("ERROR")