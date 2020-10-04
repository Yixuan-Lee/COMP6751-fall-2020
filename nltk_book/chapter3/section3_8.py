"""
Chapter 3 section 3.8: Segmentation

website: http://www.nltk.org/book/ch03.html

"""

import nltk
import pprint
from nltk.corpus import brown

# ## sentence segmentation
print('--------------------- a. ------------------------')
# print(len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents()))

# ## sentence segmenter
# nltk.download('gutenberg')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = nltk.sent_tokenize(text)
pprint.pprint(sents[79:89])

