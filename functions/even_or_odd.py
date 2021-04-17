def even(num1):
    if num1 % 2 == 0:
        return 0
    else:
        return 1


num = int(input("enter a number: "))
ans = even(num)
if ans == 0:
    print("even")
else:
    print("odd")

