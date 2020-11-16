import nltk

# TODO: download opinion_lexicon and sentence_polarity modules
# TODO: uncomment these before submission
# nltk.download('opinion_lexicon')
# nltk.download('sentence_polarity')

from nltk.corpus import opinion_lexicon
from nltk.corpus import sentence_polarity
from typing import Dict


class Polarity:
    def __init__(self):
        # negative words
        self.negative_lexica = opinion_lexicon.negative()
        self.negative_lexica_size = len(self.negative_lexica)
        # positive words
        self.positive_lexica = opinion_lexicon.positive()
        self.positive_lexica_size = len(self.positive_lexica)

        # sentence sentiment categories
        self.senti_categories = sentence_polarity.categories()

    def get_lexica_polarity(self, sent: str) -> Dict[str, str]:
        """
        return the polarity for each token in the sentence in a dictionary
        :param sent: sentence
        :return: a dictionary containing the polarity
        """
        sent = sent.replace(',', '')[:-1].rstrip()
        tokens = sent.split(' ')
        polarity = {}
        for t in tokens:
            if t in self.negative_lexica:
                polarity[t] = 'negative'
            elif t in self.positive_lexica:
                polarity[t] = 'positive'
            else:
                polarity[t] = 'neutral'
        return polarity


def print_polarity(mmap: Dict[str, str]) -> None:
    for key, value in mmap.items():
        print(key, '\t:\t', value)


if __name__ == '__main__':
    pol = Polarity()
    print_polarity(pol.get_lexica_polarity("this may not have the dramatic gut-wrenching impact of other holocaust films , but it's a compelling story , mainly because of the way it's told by the people who were there ."))
    print('-------------------------------------')
    print_polarity(pol.get_lexica_polarity("a perfect example of rancid , well-intentioned , but shamelessly manipulative movie making ."))
    print('-------------------------------------')
    print_polarity(pol.get_lexica_polarity("it's a compelling story , but it has low impact ."))
    print('-------------------------------------')
    print_polarity(pol.get_lexica_polarity("this does not have gut-wrenching impact but it's a compelling story ."))
    # print('-------------------------------------')
    # print_polarity(pol.get_lexica_polarity("rancid movie making ."))
    # print('-------------------------------------')
    # print_polarity(pol.get_lexica_polarity("it has low impact ."))

