# HOW TO INVOKE A FUNCTION FROM ANOTHER PYTHON FILE


# METHOD 1
#
# import functions.operation
#
# sum = functions.operation.add(10,20)
# print(sum)
#
# dif = functions.operation.sub(10,20)
# print(dif)
#
# prod = functions.operation.mul(10,20)
# print(prod)
#
# res = functions.operation.div(10,20)
# print(res)
#


# METHOD 2

from functions.operation import *

sum = add(15, 20)
print(sum)

dif = sub(15, 20)
print(dif)

prod = mul(15, 25)
print(prod)

quo = div(15, 20)
print(quo)
