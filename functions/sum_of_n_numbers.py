def sum1(num):
    s = 0
    for i in range(0, num + 1):
        s += i
    return s


num = int(input("enter a number: "))
sum = sum1(num)
print(sum)
