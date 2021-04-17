# ALGORITHM

# 1. sort the list/array
# 2. define variables low = 0 AND upp = (length of list-1)
# 3. calculate midvalue => mid = (low+upp)//2
# 4. conditions:
#   I] if element > lst[mid]:
#           low = mid +1
#   II] if element < lst[mid]:
#           upp = mid - 1
#   III] if element == lst[mid]:
#           element found

lst = [3, 4, 2, 11, 10, 13, 12, 14, 15]
lst.sort()
print(lst)
low = 0
upp = len(lst) - 1
element = int(input("enter element to search : "))
flag = 0
while low <= upp:
    mid = (low + upp) // 2
    if element > lst[mid]:
        low = mid + 1
    elif element < lst[mid]:
        upp = mid - 1
    else:
        flag = 1
        break
if flag == 1:
    print("FOUND")
else:
    print("NOT FOUND")
