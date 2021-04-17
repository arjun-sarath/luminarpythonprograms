# def func_name(arguments):
#     function definition
#
# function call is done using function name

# 1. function without arguments and no return type
# 2. function with arguments and no return type
# 3. function with arguments and return type

# 1.

# def sub():
#     num1 = int(input("enter num1: "))
#     num2 = int(input("enter num2: "))
#     dif = num1 - num2
#     print(dif)
# sub()

# def mul():
#     num1 = int(input("enter num1: "))
#     num2 = int(input("enter num2: "))
#     prod = num1 * num2
#     print(prod)
# mul()

# 2.

# def add(num1, num2):
#     sum = num1 + num2
#     print(sum)
#
# add(30, 50)

# def sub(num1, num2):
#     dif = num1 - num2
#     print(dif)
#
# sub(30, 50)

# def mul(num1, num2):
#     prod = num1 * num2
#     print(prod)
#
# mul(30, 50)

# 3.

# def add(num1, num2):
#     sum = num1 + num2
#     return sum
#
# sum = add(30, 50)
# print(sum)

# def sub(num1, num2):
#     dif = num1 - num2
#     return dif
#
# ans = sub(30, 50)
# print(ans)

def mul(num1, num2):
    prod = num1 * num2
    return prod

product = mul(30, 50)
print(product)