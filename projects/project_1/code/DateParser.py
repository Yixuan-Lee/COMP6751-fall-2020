import nltk
from typing import List, Set


class DateParser:

    def __init__(self, sentences: List[str], pos_taggings: List[List[str]]):
        self.sents = sentences
        self.pos_tags = pos_taggings

    def date_parse(self, dates: Set[str]):
        # support formats:
        #   2020-12-12
        #   2020/12/12
        #   December 2
        #   December 12
        #   December 12th
        #   December 12th 2020
        #   the twelfth of December
        #   the 12th of December
        #   in 2020
        DateParseCFG = nltk.CFG.fromstring("""
            DATE -> YEAR SEP MONTH_NUM SEP DAY | MONTH_STR DAY | MONTH_STR NN_NUM | MONTH_STR NN_NUM YEAR | DT NN_STR IN MONTH_STR | DT NN_NUM IN MONTH_STR | IN YEAR
            SEP -> "/" | "-"
            YEAR -> DIGIT DIGIT DIGIT DIGIT
            MONTH_NUM -> DIGIT | DIGIT DIGIT
            DAY -> DIGIT | DIGIT DIGIT
            DT -> "the"
            IN -> "of" | "in"
            NN_STR -> "first" | "second" | "third" | "fourth" | "fifth" | "sixth" | "seventh" | "eighth" | "ninth" | "tenth" | "eleventh" | "twelfth" | "thirteenth" | "fourteenth" | "fifteenth" | "sixteenth" | "seventeenth" | "eighteenth" | "nineteenth" | "twentieth" | "twenty-first" | "twenth-second" | "twenty-third" | "twenty-fourth" | "twenty-fifth" | "twenty-sixth" | "twenty-seventh" | "twenty-eighth" | "twenth-ninth" | "thirtieth" | "thirty-first"
            MONTH_STR -> "January" | "February" | "March" | "April" | "May" | "June" | "July" | "August" | "September" | "October" | "November" | "December"
            NN_NUM -> "1st" | "2nd" | "3rd" | "4th" | "5th" | "6th" | "7th" | "8th" | "9th" | "10th" | "11th" | "12th" | "13th" | "14th" | "15th" | "16th" | "17th" | "18th" | "19th" | "20th" | "21st" | "22nd" | "23rd" | "24th" | "25th" | "26th" | "27th" | "28th" | "29th" | "30th" | "31st"
            DIGIT -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
            """)
        date_parser = nltk.ChartParser(DateParseCFG)

        for date in dates:
            if date.find('/') != -1:
                # if the format is yyyy/mm/dd then each character is a token
                tokens = [ch for ch in date]
            else:
                tokens = []
                for t in date.split():
                    if t.isnumeric():
                        tokens.extend([num for num in t])
                    else:
                        tokens.append(t)

            for tree in date_parser.parse(tokens):
                print(tree)
                # tree.draw()

        # date examples
        # sentence1 = [char for char in "2020/12/25"]
        # sentence2 = "December 25th".split()
        # sentence3 = "the twenty-fifth of December".split()
        # sentence4 = "the 25th of December".split()
        # print('9. ---------------------------------------------')
        # print(sentence1)
        # print(sentence2)
        # print(sentence3)
        # print(sentence4)
        # for tree in date_parser.parse(sentence1):
        #     print(tree)
        #     tree.draw()
        # for tree in date_parser.parse(sentence2):
        #     print(tree)
        #     tree.draw()
        # for tree in date_parser.parse(sentence3):
        #     print(tree)
        #     tree.draw()
        # for tree in date_parser.parse(sentence4):
        #     print(tree)
        #     tree.draw()
