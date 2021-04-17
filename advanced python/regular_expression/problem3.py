# min length 8 and max length 15 (no nos.)

import re
data = input("enter the data : ")
rule = "\D{8,15}"
matcher = re.fullmatch(rule, data)
if matcher is not None:
    print("Valid")
else:
    print("Invalid")
