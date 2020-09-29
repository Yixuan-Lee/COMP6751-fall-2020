import re
import nltk
from nltk import RegexpParser
from nltk import RegexpTokenizer

sents = 'This year is March 30. The Christmas day is on December 25th, 2020, and the New Year\'s Day is on 2020-01-01 or 2020/01/01. And I have 2020 apples.'

sentences = nltk.sent_tokenize(sents)
for s in sentences:
    words = nltk.word_tokenize(s)
    print(nltk.pos_tag(words))

#
# grammar = r"""
#     DATE:   {<NNP> <CD> <,>? <CD>}  # E.g. December 12th, 2020
#             {<DT> <NN> <IN> <NNP>}  # E.g. the twelfth of December
#             {<DT> <CD> <IN> <NNP>}  # E.g. the 12th of December
#             {<NNP> <CD>}            # E.g. December 12th
#             {<IN> <CD>}             # E.g. in 2020, on 2020/12/12
#             {<IN> <JJ>}             # E.g. on 2020-12-12
# """
# cp = RegexpParser(grammar)

# pattern = r'''
#     (\d{4}((-|/)\d{2}(-|/)\d{2})?)          # 2020, 2020-12-12, 2020/12/12
#     | (\w \d{1,2}(st|nd|rd|th)(,? \d{4})?)  # December 12th, December 12th 2020, December 12th, 2020
#     | (the \w of \w)                        # the twelfth of December
#     | (the \d{1,2}(st|nd|rd|th) of \w)      # the 12th of December
# '''
# p = re.compile('(\d{4}[-/]?\d{2}[-/]?\d{2})')     #1
# print(p.findall('2020-12-20'))
# print(p.findall('2020/12/20'))

# p = re.compile("(\w+\s\d{1,2}[a-zA-Z]{2},?\s?\d{4}?)")    #2
# print(p.findall('December 20th 2020'))
# print(p.findall('December 22nd, 2020'))

# p = re.compile("(the\s\d{1,2}[a-zA-Z]{2}\sof\s[a-zA-Z]+)")    #3
# print(p.findall('the 12th of December'))
# print(p.findall('the 1st of December'))

# p = re.compile("(the\s\w+\sof\s\w+)")     #4
# print(p.findall('the twelfth of December'))

# p = re.compile("(\w+\s\d{1,2}[a-zA-Z]{2})")   #5
# print(p.findall('December 2nd'))

p = re.compile("(\w+\s\d{1,2})")   #6
print(p.findall('December 2'))
print(p.findall('at 1.32'))


# pattern = "(\d{4}[-/]?\d{2}[-/]?\d{2})"\
#                "|(\w+\s\d{1,2}[a-zA-Z]{2},?\s?\d{4}?)"\
#                "|(the\s\d{1,2}[a-zA-Z]{2}\sof\s[a-zA-Z]+)"\
#                "|(the\s\w+\sof\s\w+)"\
#                "|(\w+\s\d{1,2}[a-zA-Z]{2})"\
#                "|(\w+\s\d{1,2})"
# p = re.compile(pattern)
# print(p.findall('2020-12-20'))
# print(p.findall('2020/12/20'))
# print(p.findall('December 20th 2020'))
# print(p.findall('December 22nd, 2020'))
# print(p.findall('the 12th of December'))
# print(p.findall('the 1st of December'))
# print(p.findall('the twelfth of December'))
# print(p.findall('December 2nd'))
# print(p.findall('December 2'))
# print(p.findall('at 1.32'))

