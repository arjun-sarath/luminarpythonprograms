# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
#
# res = add(10, 20, 30)
# print(res)

# ***************************************

# def print_person_details(*args):   # here args contains arguments as tuple
#     print(args)
#
#
# print_person_details("ajay", "thrissur", "kakkanad")

# ***************************************

# def print_person_details(**kwargs):   # here kwargs contains keyvalue pairs of arguments passed (dictionary format)
#     print(kwargs)
#
#
# print_person_details(name = "ajay", birthplace = "thrissur", workplace = "kakkanad")

# ***************************************

# lst = [10, 15, 8, 20, 23, 20]
# lst.sort(reverse=True)             # sort in descending order
# print(lst)

# ***************************************

# employees = {
#     1000: {'name': 'sajay', 'desig': 'python trainer', 'experience': '3'},
#     1001: {'name': 'sabir', 'desig': 'bigdata trainer', 'experience': '2'},
#     1002: {'name': 'christy', 'desig': 'ml', 'experience': '3'}
#
# }
#
# eid = int(input('enter employee id: '))
# if eid in employees:
#     # print('eid exists')
#     print(employees[eid]['name'])
# else:
#     print('eid not exist')

# *******************************************


employees = {
    1000: {'name': 'sajay', 'desig': 'python trainer', 'experience': '3'},
    1001: {'name': 'sabir', 'desig': 'bigdata trainer', 'experience': '2'},
    1002: {'name': 'christy', 'desig': 'ml', 'experience': '3'}
}


def emp_details(**kwargs):    # kwargs = {eid:100, prop:'desig'}
    id = kwargs['eid']
    prop = kwargs['prop']  #desig
    if id in employees:
        print(employees[id]['name'])
        print(employees[id][prop])
    else:
        print('eid not exist')


emp_details(eid=1000, prop='desig')
