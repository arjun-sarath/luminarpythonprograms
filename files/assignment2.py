f = open(r"C:\Users\User\Desktop\customer", "r")
position = {}
for lines in f:
    data = lines.rstrip("\n").split(",")
    if data[4] not in position:
        position[data[4]] = 1
    else:
        position[data[4]] += 1
print(position)