num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
if (num1 == num2) & (num2 == num3):
    print("All are Equal")
else:
    if (num1 > num2) & (num1 > num3):
        if num2 > num3:
            print("Second highest is: ", num2)
        else:
            print("Second highest is: ", num3)
    elif (num2 > num1) & (num2 > num3):
        if num1 > num3:
            print("Second highest is: ", num1)
        else:
            print("Second highest is: ", num3)
    else:
        if num1 > num2:
            print("Second highest is: ", num1)
        else:
            print("Second highest is: ", num2)
