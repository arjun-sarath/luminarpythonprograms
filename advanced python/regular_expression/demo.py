# regular expression

# re -- package for pattern matching

# import re
#
# count = 0
# matcher = re.finditer("ab", "abaabbab")           # here all "ab" in "abaabbab" combinations are stored in matcher
# for match in matcher:
#     count += 1
# print("count:", count)



import re

count = 0
matcher = re.finditer("ab", "abaabbab")           # here all "ab" in "abaabbab" combinations are stored in matcher
for match in matcher:
    print("match available at", match.start())    # to get starting position of match
    print("group =", match.group())               # to print the matched data
    count += 1
print("count:", count)

