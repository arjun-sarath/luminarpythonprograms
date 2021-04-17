lst = [1, 2, 3, 4, 5, 6]
lst1 = []
num = int(input("enter the number : "))
flag = 0
for i in lst:
    for j in lst:
        if i + j == num:
            lst1.append([i, j])
            flag = 1
            break
print(lst1)
