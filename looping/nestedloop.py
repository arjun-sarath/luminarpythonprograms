# for i in range(1, 4):
#     for j in range(1, 4):                                      # 1 1 1
#         print(i, end=" ")  # to seperate elements with space   # 2 2 2
#     print()    # to go to new line                             # 3 3 3

# for i in range(1, 4):
#     for j in range(1,4):        # 1 2 3
#         print(j, end=" ")       # 1 2 3
#     print()                     # 1 2 3

# for i in range(1, 6):               # 1
#     for j in range(1, i + 1):       # 1 2
#         print(j, end=" ")           # 1 2 3
#     print()                         # 1 2 3 4
#                                     # 1 2 3 4 5

# for i in range(0, 10):
#     for j in range(10 - i, 0, -1):
#         print(j, end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(6 - i, 0, -1):
#         print(i, end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print(i, end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print(5, end=" ")
#     print()

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
