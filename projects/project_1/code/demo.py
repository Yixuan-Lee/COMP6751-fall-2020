import nltk
from nltk.tokenize import RegexpTokenizer

text = 'The percentages are 25.22% and 300%.'
pattern = r'''(?x)      # set flag to allow verbose regexps
    (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A., U.S.
    | \d+(?:\.\d+)?%?
    | \w+
'''

regex_tokenizer = RegexpTokenizer(pattern)
print(regex_tokenizer.tokenize(text))
print('------------------------------------------------------------')

sent = "the fifth of November"
print(nltk.pos_tag(nltk.word_tokenize(sent)))

import re
sentence1 = re.split('(/)', "2020/12/25")
print(sentence1)


from nltk import word_tokenize
print(word_tokenize("John's big idea isn't all that bad."))
print(nltk.pos_tag(word_tokenize("John's big idea isn't all that bad.")))