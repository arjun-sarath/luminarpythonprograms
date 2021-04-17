lst = [10, 20, 30, 40, 50]
element = int(input("enter the element to search: "))
flag = 0
for i in lst:
    if i == element:
        flag = 1
        break
if flag == 1:
    print("FOUND")
else:
    print("NOT FOUND")

# drawback of linear search : complexity is high