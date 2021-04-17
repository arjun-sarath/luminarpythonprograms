# def decorator_sub(func):
#     def inner(n1, n2):
#         if n1 < n2:
#             n1, n2 = n2, n1
#         return func(n1, n2)
#
#     return inner
#
#
# @decorator_sub
# def sub(num1, num2):
#     return num1 - num2
#
#
# res = sub(8, 10)
# print(res)

# ***********************************************************

def decorator_div(func):
    def inner(n1, n2):
        if n1 < n2:
            n1, n2 = n2, n1
        return func(n1, n2)

    return inner


@decorator_div
def div(num1, num2):
    return num1/num2


res = div(8, 10)
print(res)
