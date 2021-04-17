lst = []

# append : used to add elements to list

lst.append(10)
# print(lst)

lst.append("rooney")
# print(lst)

lst.append("manchester united")
# print(lst)

# lst.append(10, 15, 100)       # error : append can take only one element at a time, hence we go for extend
# print(lst)

# extend          =>    to add multiple elements to list

lst.extend([10, 15, 20])
print(lst)