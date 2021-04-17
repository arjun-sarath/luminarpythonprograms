# combination of upper and lower case letters ending with a number

import re
data = input("enter the data : ")
rule = "[a-zA-z]+\d$"
matcher = re.fullmatch(rule, data)
if matcher is not None:
    print("Valid")
else:
    print("Invalid")