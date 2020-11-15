import os
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
        self.positive_sentences = []
        self.negative_sentences = []

        response1 = input('Would you want to test sentiment with a local text data? (Y/N) ')
        if response1.lower() == 'y' or response1.lower() == 'yes':
            positive_file = input('Input the path for the positive sentiment data: ')
            negative_file = input('Input the path for the negative sentiment data: ')
            if os.path.exists(positive_file):
                # read positive sentences
                with open(positive_file, "r") as reader:
                    self.positive_sentences = reader.readlines()
                self.positive_sentences = [sent.rstrip() for sent in self.positive_sentences]
            if os.path.exists(negative_file):
                # read negative sentences
                with open(negative_file, "r") as reader:
                    self.negative_sentences = reader.readlines()
                self.negative_sentences = [sent.rstrip() for sent in self.negative_sentences]
        else:
            # use 5331 positive sentences and 5331 negative sentences as testing data
            # since this requires a huge amount of lexica, so this part is not implemented
            response2 = input('Would you want to test sentiment with data in sentence_polarity? (Y/N) ')
            if response2.lower() == 'y' or response2.lower() == 'yes':
                # negative words
                self.negative_lexica = opinion_lexicon.negative()
                self.negative_lexica_size = len(self.negative_lexica)
                # positive words
                self.positive_lexica = opinion_lexicon.positive()
                self.positive_lexica_size = len(self.positive_lexica)

                # sentence sentiment categories
                self.senti_categories = sentence_polarity.categories()
                # negative sentiment sentences
                self.negative_sentences = sentence_polarity.sents(categories=['neg'])[:10]  # get the first 10 sentences
                self.negative_sentences = [' '.join(sent) for sent in self.negative_sentences]
                self.negative_sentences_size = len(self.negative_sentences)
                # positive sentiment sentences
                self.positive_sentences = sentence_polarity.sents(categories=['pos'])[:10]  # get the first 10 sentences
                self.positive_sentences = [' '.join(sent) for sent in self.positive_sentences]
                self.positive_sentences_size = len(self.positive_sentences)

    def get_negative_sents(self) -> List[str]:
        return self.negative_sentences

    def get_positive_sents(self) -> List[str]:
        return self.positive_sentences


## for testing DataLoader
if __name__ == '__main__':
    d = DataLoader()
    print(len(d.get_negative_sents()))
    print(len(d.get_positive_sents()))
