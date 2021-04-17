line = "hai hello hai hello hai"
print(line)

# split function : to split line into word by word

words = line.split(" ")
# print(words)
dict1 = {}
for i in words:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
for i in dict1:
    print(i, ":", dict1[i])
