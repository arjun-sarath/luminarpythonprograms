classheld = int(input("number of classes held: "))
classattended = int(input("number of classes attended: "))
percent = (classattended / classheld) * 100
print("percentage of class attended", percent)
if percent < 75:
    print("not eligible")
else:
    print("eligible")