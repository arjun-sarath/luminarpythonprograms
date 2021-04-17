# rule 1

# import re
#
# x = "[abc]"        # either a, b or c
# matcher = re.finditer(x, "abt c@5kz")          # it finds every a, b and c in "abt c@5kz" and store it in matcher
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)


# rule 2

# import re
#
# x = "[^abc]"        # not a, b or c
# matcher = re.finditer(x, "abt c@5kz")
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)


# rule 3

# import re
#
# x = "[a-z]"        # from a to z (only small letters)
# matcher = re.finditer(x, "abt c@5kz")
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)


# rule 4

# import re
#
# x = "[A-Z]"        # from capital letters A to Z
# matcher = re.finditer(x, "abT C@5kZ")
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)


# rule 5

# import re
#
# x = "[a-zA-Z]"     # both lower and upper cases are checked
# matcher = re.finditer(x, "abT C@5kZ")
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)


# rule 6
#
# x = [0-9]         # check digits
#
#
# rule 7
#
# x = [^a-zA-Z0-9]   # check special symbols


# rule 8

# import re
#
# x = "\s"     # check space
#
# matcher = re.finditer(x, "abT C@5kZ")
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)


# rule 9
#
# x = '\d'   # check digits
#
#
# rule 10
#
# x = '\D'   # except digits


# rule 11

import re

# x = "\w"        # all words expect special characters
# matcher = re.finditer(x, "abT C@5kZ")
# for match in matcher:
#     print("position:", match.start())
#     print("matched data:", match.group())
#     print("*" * 20)

# rule 12

import re

x = "\W"        # for special characters
matcher = re.finditer(x, "abT C@5kZ")
for match in matcher:
    print("position:", match.start())
    print("matched data:", match.group())
    print("*" * 20)