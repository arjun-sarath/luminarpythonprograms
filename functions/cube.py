# def cube():
#     num = int(input("enter a number: "))
#     ans = num * num * num
#     print(ans)
#
# cube()


# def cube(num):
#     ans = num ** num
#     print(ans)
#
# num = int(input("enter a number: "))
# cube(num)


def cube(num):
    ans = num ** num
    return ans

num = int(input("enter a number: "))
cube1 = cube(num)
print(cube1)