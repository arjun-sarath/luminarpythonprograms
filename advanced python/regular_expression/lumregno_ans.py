import re
f1 = open("lumregno", "r")
f2 = open("pythonstudents", "w")
rule = "[L][U][M]\d{2}[P][Y]\d{3}"
for lines in f1:
    regno = lines.rstrip("\n")
    matcher = re.fullmatch(rule, regno)
    if matcher is not None:
        f2.write(regno)
        f2.write("\n")
