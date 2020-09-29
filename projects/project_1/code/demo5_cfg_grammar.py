import nltk
import re

DateParseCFG = nltk.CFG.fromstring(r"""
    DATE -> MONTH_STR DAY | IN YEAR_NUM
    IN -> "in"
    YEAR_NUM -> DIGIT DIGIT DIGIT DIGIT
    MONTH_STR -> "January" | "February" | "March" | "April" | "May" | "June" | "July" | "August" | "September" | "October" | "November" | "December"
    DAY -> DIGIT | DIGIT DIGIT
    DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    """)
parser = nltk.ChartParser(DateParseCFG)
digits = "January 23".split()
digits = ['in', '2', '0', '1', '3']
print(digits)
print(nltk.pos_tag(digits))
# digits = [char for char in digits]
# print(digits)

print(parser.parse(digits))
for tree in parser.parse(digits):
    print(tree)
    tree.draw()

