# common elements

# lst1 = [10, 20, 30, 40]
# lst2 = [11, 12, 20, 30]
# lst3 = []
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             lst3.append(i)
# print(lst3)

lst1 = [10, 20, 30, 40]
lst2 = [11, 12, 20, 30]
lst3 = [i for i in lst1 for j in lst2 if i == j]
print(lst3)

