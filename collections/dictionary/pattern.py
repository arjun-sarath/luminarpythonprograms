pattern = "ABCDBCA"
print(pattern)
dict1 = {}
for i in pattern:
    if i not in dict1:
        dict1[i] = 1
    else:
        print("first recursive element : ", i)
        break
