f = open(r"C:\Users\User\Desktop\customer", "r")
age = {}
for lines in f:
    data = lines.rstrip("\n").split(",")
    if data[3] not in age:
        age[data[3]] = 1
    else:
        age[data[3]] += 1
print(age)