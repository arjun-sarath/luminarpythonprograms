# def factorial():
#     num = int(input("enter a number: "))
#     fact = 1
#     for i in range(1,num + 1):
#         fact *= i
#     print(fact)
#
#
# factorial()


# def factorial(num):
#     fact = 1
#     for i in range(1,num + 1):
#             fact *= i
#     print(fact)
#
#
# num = int(input("enter a number: "))
# factorial(num)


def factorial(num):
    fact = 1
    if num == 0:
        return fact
    else:
        for i in range(1, num + 1):
            fact *= i
        return fact


num = int(input("enter the number: "))
fact = factorial(num)
print(fact)
