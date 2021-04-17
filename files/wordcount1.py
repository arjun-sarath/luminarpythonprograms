f = open("data", "r")
dict1 = {}
for lines in f:
    words = lines.rstrip().split(" ")      # to remove next line character (\n) after each line and split each words and store it to words
    for word in words:
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
print(dict1)
