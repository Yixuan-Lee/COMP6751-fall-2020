import re

str = "aoweijriow aofejofenr wajioejfo er (!#^ &% etc@ 3 $ $%#) wearjwoaieraw awoerj oawier"

p = re.compile('\(.*\)')
print(p.findall(str))

print("22th".isalnum())


from nltk import regexp_tokenize
txt = "Today it's 07.May 2011. Or 2.999."
print(regexp_tokenize(txt, pattern=r'\w+([.,]\w+)*|\S+'))
