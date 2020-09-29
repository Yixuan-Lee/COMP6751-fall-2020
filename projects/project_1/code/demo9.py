import re

str = "aoweijriow aofejofenr wajioejfo er (!#^ &% etc@ 3 $ $%#) wearjwoaieraw awoerj oawier"

p = re.compile('\(.*\)')
print(p.findall(str))

print("22th".isalnum())
