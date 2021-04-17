# lst1 = [1, 2, 3, 4]

# squares = [num ** 2 for num in lst1]
# evens = [num for num in lst1 if num % 2 == 0]
# print(squares)
# print(evens)

lst1 = [1, 2]
lst2 = [10, 20]
# pairs = []
# for i in lst1:
#     for j in lst2:
#         pairs.append((i, j))
pairs = [(i, j) for i in lst1 for j in lst2]
print(pairs)