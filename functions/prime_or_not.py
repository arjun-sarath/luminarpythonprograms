def prime(num1):
    count = 0
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0


num = int(input("enter a number: "))
ans = prime(num)
if ans == 1:
    print("prime")
else:
    print("not prime")

