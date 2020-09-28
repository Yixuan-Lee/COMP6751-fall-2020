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
