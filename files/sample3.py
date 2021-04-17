f = open("numbers", "r")
even = []
odd = []

for num in f:
    if int(num) % 2 == 0:
        even.append(int(num.rstrip("\n")))
    else:
        odd.append(int(num.rstrip("\n")))
print("sum of even num : ", sum(even))
print("sum of odd num : ", sum(odd))
