import nltk
import re

DateParseCFG = nltk.CFG.fromstring("""
            DATE -> IN YEAR SEP MONTH_NUM SEP DAY | YEAR SEP MONTH_NUM SEP DAY | MONTH_STR DAY SEP YEAR | MONTH_STR DAY | MONTH_STR YEAR | IN MONTH_STR NN_NUM | MONTH_STR NN_NUM YEAR | MONTH_STR NN_NUM SEP YEAR | MONTH_STR NN_NUM | DT NN_STR IN MONTH_STR | DT NN_NUM IN MONTH_STR | IN YEAR | IN MONTH_STR YEAR
            SEP -> "/" | "-" | ","
            YEAR -> DIGIT DIGIT DIGIT DIGIT
            MONTH_NUM -> DIGIT | DIGIT DIGIT
            DAY -> DIGIT | DIGIT DIGIT
            DT -> "the"
            IN -> "of" | "in" | "on"
            NN_STR -> "first" | "second" | "third" | "fourth" | "fifth" | "sixth" | "seventh" | "eighth" | "ninth" | "tenth" | "eleventh" | "twelfth" | "thirteenth" | "fourteenth" | "fifteenth" | "sixteenth" | "seventeenth" | "eighteenth" | "nineteenth" | "twentieth" | "twenty-first" | "twenth-second" | "twenty-third" | "twenty-fourth" | "twenty-fifth" | "twenty-sixth" | "twenty-seventh" | "twenty-eighth" | "twenth-ninth" | "thirtieth" | "thirty-first"
            MONTH_STR -> "January" | "February" | "March" | "April" | "May" | "June" | "July" | "August" | "September" | "October" | "November" | "December"
            NN_NUM -> "1st" | "2nd" | "3rd" | "4th" | "5th" | "6th" | "7th" | "8th" | "9th" | "10th" | "11th" | "12th" | "13th" | "14th" | "15th" | "16th" | "17th" | "18th" | "19th" | "20th" | "21st" | "22nd" | "23rd" | "24th" | "25th" | "26th" | "27th" | "28th" | "29th" | "30th" | "31st"
            DIGIT -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
            """)
parser = nltk.ChartParser(DateParseCFG)
sentence1 = "in December 2020"


if sentence1.find('/') != -1 or sentence1.find('-') != -1:
    tokens = [ch for ch in sentence1]
else:
    tokens = []
    for t in sentence1.split():
        if t.isnumeric():
            tokens.extend([num for num in t])
        else:
            tokens.append(t)
print('tokens: ', tokens)

for tree in parser.parse(tokens):
    tree.draw()
