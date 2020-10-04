import nltk
import re

DateParseCFG = nltk.CFG.fromstring("""
    DATE -> YEAR_NUM SEP MONTH_NUM SEP DAY_NUM | MONTH_STR NN_NUM | DT NN_STR IN MONTH_STR | DT NN_NUM IN MONTH_STR
    SEP -> "/"
    YEAR_NUM -> DIGIT DIGIT DIGIT DIGIT
    MONTH_NUM -> DIGIT | DIGIT DIGIT
    DAY_NUM -> DIGIT | DIGIT DIGIT
    DT -> "the"
    IN -> "of"
    NN_STR -> "first" | "second" | "third" | "fourth" | "fifth" | "sixth" | "seventh" | "eighth" | "ninth" | "tenth" | "eleventh" | "twelfth" | "thirteenth" | "fourteenth" | "fifteenth" | "sixteenth" | "seventeenth" | "eighteenth" | "nineteenth" | "twentieth" | "twenty-first" | "twenth-second" | "twenty-third" | "twenty-fourth" | "twenty-fifth" | "twenty-sixth" | "twenty-seventh" | "twenty-eighth" | "twenth-ninth" | "thirtieth" | "thirty-first"
    MONTH_STR -> "January" | "February" | "March" | "April" | "May" | "June" | "July" | "August" | "September" | "October" | "November" | "December"
    NN_NUM -> "1st" | "2nd" | "3rd" | "4th" | "5th" | "6th" | "7th" | "8th" | "9th" | "10th" | "11th" | "12th" | "13th" | "14th" | "15th" | "16th" | "17th" | "18th" | "19th" | "20th" | "21st" | "22nd" | "23rd" | "24th" | "25th" | "26th" | "27th" | "28th" | "29th" | "30th" | "31st"
    DIGIT -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    """)
parser = nltk.ChartParser(DateParseCFG)
sentence1 = re.split('(/)', "2020/12/25")
sentence2 = "December 25th".split()
sentence3 = "the twenty-fifth of December".split()
sentence4 = "the 25th of December".split()
print('9. ---------------------------------------------')
print(sentence1)
# print(sentence2)
# print(sentence3)
# print(sentence4)
print(parser.parse(sentence1))
# print(parser.parse(sentence2))
# print(parser.parse(sentence3))
# print(parser.parse(sentence4))

