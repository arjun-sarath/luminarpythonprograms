sub1 = int(input("enter marks of subject 1: "))
sub2 = int(input("enter marks of subject 2: "))
sub3 = int(input("enter marks of subject 3: "))
sub4 = int(input("enter marks of subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percent = (total / 200) * 100             # assuming maximum marks = 200 (50+50+50+50)
print("percentage: ", percent)
if percent >= 90:
    print("A+")
elif percent >= 80:
    print("A")
elif percent >= 70:
    print("B+")
elif percent >= 60:
    print("B")
elif percent >= 50:
    print("C+")
elif percent >= 40:
    print("C")
elif percent >= 30:
    print("D+")
else:
    print("FAIL")