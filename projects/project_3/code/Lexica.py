from nltk.corpus import opinion_lexicon
from nltk.corpus import sentence_polarity
from typing import List

# TODO: download opinion_lexicon and sentence_polarity modules
# TODO: uncomment these before submission
# nltk.download('opinion_lexicon')
# nltk.download('sentence_polarity')


class DataLoader:
    def __init__(self):
        """
        constructor
        """
        # negative words
        self.negative_lexica = opinion_lexicon.negative()
        self.negative_lexica_size = len(self.negative_lexica)
        # positive words
        self.positive_lexica = opinion_lexicon.positive()
        self.positive_lexica_size = len(self.positive_lexica)

        # sentence sentiment categories
        self.senti_categories = sentence_polarity.categories()
        # negative sentiment sentences
        self.negative_sentences = sentence_polarity.sents(categories=['neg'])
        self.negative_sentences_size = len(self.negative_sentences)
        # positive sentiment sentences
        self.positive_sentences = sentence_polarity.sents(categories=['pos'])
        self.positive_sentences_size = len(self.positive_sentences)

    def get_negative_sents(self) -> List[str]:
        return [' '.join(sent) for sent in self.negative_sentences]

    def get_positive_sents(self) -> List[str]:
        return [' '.join(sent) for sent in self.positive_sentences]


## for testing DataLoader
if __name__ == '__main__':
    d = DataLoader()
    print(len(d.get_negative_sents()))
    print(len(d.get_positive_sents()))
