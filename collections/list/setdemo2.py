
# to remove duplicate elements of a list

# lst = [10, 10, 20, 20, 25, 25, 85, 41, 41, 25, 58]
# lst1 = set(lst)          # type of lst1 is set
# print(lst1)

# **********************************************

employee = [[1001, "arun", 15000], [1002, "arjun", 20000], [1003, "vinu", 25000], [1004, "binu", 10000]]    # nested list

# print(employee)

# for i in employee:           # to access each row in list
#     print(i)

# for i in employee:
#     print(i[1])                # to print employee names only

# for i in employee:
#     if i[2] > 17000:             # to print names of employees whose salary > 17000
#         print(i[1])

sum = 0
for i in employee:
    sum += i[2]                    # to calculate total salary
print(sum)

