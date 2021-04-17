import re
email = input("enter the email to validate : ")
rule = "[a-zA-Z0-9_.+-]+@[a-zA-Z]+[.]\w+$"         # \. or [.] : to check dot
matcher = re.fullmatch(rule, email)
if matcher is not None:
    print("Valid")
else:
    print("Invalid")
