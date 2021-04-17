# import re
#
# n = "helloo"
# x = '\w{6}'
# match = re.fullmatch(x, n)
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

#**********************

import re

n = "56kg"
x = '\d{2}[a-z]{2}'
matcher = re.fullmatch(x, n)
if matcher is not None:
    print("Valid")
else:
    print("Invalid")