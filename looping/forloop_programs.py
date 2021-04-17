# for i in range(10, -1, -1):            # print from 10 to 0
#     print(i)

# low = int(input("enter lower limit: "))
# upp = int(input("enter upper limit: "))
# for i in range(low, upp + 1):           # print numbers from low to upp
#     print(i)

# low = int(input("enter lower limit: "))
# upp = int(input("enter upper limit: "))
# for i in range(low, upp + 1):           # print numbers from low to upp
#     if i % 2 == 0:
#         print(i)

# low = int(input("enter lower limit: "))
# upp = int(input("enter upper limit: "))
# s_even = 0
# s_odd = 0
# for i in range(low, upp + 1):            # to calculate sum of even and odd numbers
#     if i % 2 == 0:
#         s_even += i
#     else:
#         s_odd += i
# print("sum of even numbers: ", s_even)
# print("sum of odd numbers: ", s_odd)

# num = int(input("enter a number: "))
# flag = 0
# for i in range(2, num):                   # to check whether the number is prime or not
#     if num % i == 0:
#         flag = 1
#         break
# if flag == 0:
#     print("It is a prime number")
# else:
#     print("It is not a prime number")


low = int(input("enter lower limit: "))
upp = int(input("enter upper limit: "))
for i in range(low, upp + 1):
    flag = 0
    for j in range(1, i + 1):               # print all prime numbers between 2 numbers
        if i % j == 0:
            flag += 1
    if flag == 2:
        print(i)
