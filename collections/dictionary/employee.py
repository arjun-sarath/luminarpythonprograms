
employee = {"id": 1001, "ename": "arjun", "designation": "manager", "salary": 25000}

print(employee["ename"])           # to print employee name

print("company" in employee)       # to check whether key "company" available in employee

employee["company"] = "luminar"    # to add key "company" to employee dictionary
print(employee)

employee["salary"] += 15000        #

for i in employee:
    print(i, ":", employee[i])

