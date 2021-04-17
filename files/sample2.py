f = open("numbers", "r")
lst = []
for num in f:
    lst.append(int(num.rstrip("\n")))
print(lst)

# rstrip : to remove characters at the end e.g. "\n"
# lstrip : to remove characters in front

print(sum(lst))
