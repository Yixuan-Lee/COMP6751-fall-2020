"""
demo code in Project3 instruction
"""

import nltk
from nltk.corpus import opinion_lexicon
from nltk.corpus import sentence_polarity

# TODO: add these lines to project3 main file
# nltk.download('opinion_lexicon')
# nltk.download('sentence_polarity')

if __name__ == '__main__':
    # opionion_lexicon
    print('opinion lexicon:')
    print(opinion_lexicon.words()[:4])
    print(len(opinion_lexicon.words()))
    ## negative lexicon
    print('negative lexicon:')
    print(opinion_lexicon.negative()[:4])
    print(len(opinion_lexicon.negative()))
    ## positive lexicon
    print('positive lexicon:')
    print(opinion_lexicon.positive()[:4])
    print(len(opinion_lexicon.positive()))
    print()

    print('-------------------------------------------------------')

    # sentence polarity
    print('all sentences:')
    print(sentence_polarity.sents())
    print(len(sentence_polarity.sents()))

    print('sentence categories:')
    print(sentence_polarity.categories())

    print('examples:')
    print(sentence_polarity.sents()[0])
    print(sentence_polarity.sents()[10661])
    print(len(sentence_polarity.sents()))
    print()

    print('-------------------------------------------------------')

    # negative sentences in sentence_polarity
    print('negative sentences:')
    print(sentence_polarity.sents(categories=['neg']))
    print(len(sentence_polarity.sents(categories=['neg'])))
    # positive sentences in sentence_polarity
    print('positive sentences:')
    print(sentence_polarity.sents(categories=['pos']))
    print(len(sentence_polarity.sents(categories=['pos'])))

    # print('Done')
