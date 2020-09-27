import nltk
from nltk import word_tokenize

# download and import reuters corpus
# nltk.download('reuters')
from nltk.corpus import reuters


raw = reuters.raw('training/267')
print(raw)
print('---------------------------------------------')
tokens = word_tokenize(raw)
print(tokens)

############################ Pipeline ############################
# 1. tokenization



