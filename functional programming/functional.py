# lambda function

# def add(num1, num2):
#     return num1 + num2

# f = lambda num1, num2 : num1 + num2
# res = f(10, 20)
# print(res)


# cube = lambda num: num ** 3
# res = cube(3)
# print(res)


# map()
# filter()
# reduce()

# lst = [10, 20, 30, 21, 22]
# squ = []
# for num in lst:
#     res = num ** 2
#     squ.append(res)
# print(squ)

# or

lst = [10, 20, 30, 21, 22]

squares = list(map(lambda no: no ** 2, lst))         # new list "squares" with squared nos from list lst is created using map and lambda
print(squares)
cubes = list(map(lambda no: no ** 3, lst))
print(cubes)