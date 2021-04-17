# n1 = int(input("enter num1 : "))
# n2 = int(input("enter num2 : "))
# try:
#     res = n1 / n2
#     print(res)
# except:
#     print("exception occurred")

# when n2 is 0, error occurs and except statement proceeds

# ***********************************

# lst = [1, 2, 3]
# try:
#     i = int(input("enter index : "))
#     print(lst[i])
# except Exception as e:
#     print("exception occurred")

# ************************************

# VALUE ERROR

# try:
#     a = int(input("enter no : "))
#     print("entered num : ", a)
# except ValueError:
#     print("please enter an integer value")

# **************************************

lst = [1, 2, 3]
i = int(input("enter index : "))
try:
    print(lst[i])
except Exception as e:
    print("exception occurred")
finally:                              # The finally block will be executed no matter if the try block raises an error or not.
    print("inside finally")
