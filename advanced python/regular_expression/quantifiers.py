# 1.

# import re
#
# x = 'a+'      # a including group
# r = 'aaa abc aaaa cga'
#
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


# 2.

# import re
#
# x = 'a*'      # count including zero number of a
# r = 'aaa abc aaaa cga'
#
# matcher = re.finditer(x, r)
# for match in matcher:
#     print("pos:", match.start())
#     print('group:', match.group())


# 3.

import re

x = 'a?'          # count a as each including zero number at a
r = 'aaa abc aaaa cga'

matcher = re.finditer(x, r)
for match in matcher:
    print("pos:", match.start())
    print('group:', match.group())


# 4.

# import re
#
# x = 'a{3}'      # no. of 'a' position; 3 a together
# r = 'aaa abc aaaa cga'
#
# matcher = re.finditer(x, r)
# for match in matcher:
#     print("pos:", match.start())
#     print('group:', match.group())


# 5.

import re

# x = "a{1, 3}"      # minimum 1 a and maximum 3 a groups
# r = "aba abc aaaa cga"
#
# matcher = re.finditer(x, r)
# for match in matcher:
#     print("pos:", match.start())
#     print('group:', match.group())


# 6.

# import re
#
# x = '^a'      # check starting with a
# r = 'aaa abc aaaa cga'
#
# matcher = re.finditer(x, r)
# for match in matcher:
#     print("pos:", match.start())
#     print('group:', match.group())


# 7.

# import re
#
# x = "a&"     # check ending with a
# r = "aaa abc aaaa cga"
#
# matcher = re.finditer(x, r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
