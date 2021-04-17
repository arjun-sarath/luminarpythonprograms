def fibanocci(a, b, num1):
    for i in range(3, num1 + 1):
        t = a + b
        a = b
        b = t
    return(t)


num = int(input("enter a number: "))
n1 = 0
n2 = 1
if num == 1:
    print(n1)
elif num == 2:
    print(n2)
else:
    f = fibanocci(n1, n2, num)
    print(f)
