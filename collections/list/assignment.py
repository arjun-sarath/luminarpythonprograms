# lst = [3, 4, 8]         # 3+4+8=15
# lst1 = [12, 11, 7]      # 15-3, 15-4, 15-8

lst = [3, 4, 8]
print(lst)
lst1 = []
sum1 = sum(lst)
# for i in lst:
#     sum += i
for i in lst:
    lst1.append(sum1 - i)
print(lst1)
