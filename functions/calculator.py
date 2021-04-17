def add(n1, n2):
    sum = n1 + n2
    print("sum : ", sum)


def sub(n1, n2):
    dif = n1 - n2
    print("difference : ", dif)


def mul(n1, n2):
    prod = n1 * n2
    print("product : ", prod)


def div(n1, n2):
    quo = n1 / n2
    print("quotient : ", quo)


print("SELECT OPERATION \n 1 : ADDITION \n 2 : SUBSTRACTION \n 3 : MULTIPLICATION \n 4 : DIVISION")

choice = int(input("enter your choice: "))
if choice in (1, 2, 3, 4):
    num1 = int(input("enter number 1: "))
    num2 = int(input("enter number 2: "))
    if choice == 1:
        add(num1, num2)
    elif choice == 2:
        sub(num1, num2)
    elif choice == 3:
        mul(num1, num2)
    else:
        div(num1, num2)
else:
    print("WRONG CHOICE")
