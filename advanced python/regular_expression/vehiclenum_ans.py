import re
f = open("vehiclenum", "r")
rule = "[kK][lL]\d{2}[a-zA-z]{2}\d{4}$"
valid = []
for lines in f:
    num = lines.rstrip("\n")
    matcher = re.fullmatch(rule, num)
    if matcher is not None:
        valid.append(num)
print(valid)
