birth_d = int(input("enter birth date: "))
birth_m = int(input("enter birth month: "))
birth_y = int(input("enter birth year: "))

today_d = int(input("enter today date: "))
today_m = int(input("enter today month: "))
today_y = int(input("enter today year: "))

if today_m > birth_m:
    age = today_y - birth_y
elif today_m < birth_m:
    age = (today_y - birth_y) - 1
else:
    if today_d >= birth_d:
        age = today_y - birth_y
    else:
        age = (today_y - birth_y) - 1
print("age: ", age)
