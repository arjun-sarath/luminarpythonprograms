# starting with a and ending with b

import re
data = input("enter the data : ")
rule = "^a+[\w\W]*b$"
matcher = re.fullmatch(rule, data)
if matcher is not None:
    print("Valid")
else:
    print("Invalid")
