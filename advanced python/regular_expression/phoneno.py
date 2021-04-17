# import re
#
# num = input("enter the number to validate: ")
# x = '\d{10}'
# matcher = re.fullmatch(x, num)
# if matcher is not None:
#     print("Valid")
# else:
#     print("Invalid")


# ************************************

import re

num = input("enter the number to validate: ")
x = "[+][9][1]\d{10}"
matcher = re.fullmatch(x, num)
if matcher is not None:
    print("Valid")
else:
    print("Invalid")