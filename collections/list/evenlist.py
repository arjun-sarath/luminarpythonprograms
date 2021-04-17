lst = []

for i in range(50, 201):
    lst.append(i)
print("list      : ", lst)

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even list : ", even)
print("odd list  : ", odd)
