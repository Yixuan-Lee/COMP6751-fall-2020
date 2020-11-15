import os
from typing import List


class DataLoader:
    def __init__(self):
        """
        constructor
        """
        self.positive_sentences = []
        self.negative_sentences = []

        positive_filepath = input('Input the file path containing positive sentences: ')
        negative_filepath = input('Input the file path containing negative sentences: ')

        # read positive sentences
        if os.path.exists(positive_filepath):
            with open(positive_filepath, "r") as reader:
                self.positive_sentences = reader.readlines()
            self.positive_sentences = [sent.rstrip() for sent in self.positive_sentences]
        else:
            print(positive_filepath + ' does not exist on local.')

        # read negative sentences
        if os.path.exists(negative_filepath):
            with open(negative_filepath, "r") as reader:
                self.negative_sentences = reader.readlines()
            self.negative_sentences = [sent.rstrip() for sent in self.negative_sentences]
        else:
            print(negative_filepath + ' does not exist on local.')

    def get_negative_sents(self) -> List[str]:
        return self.negative_sentences

    def get_positive_sents(self) -> List[str]:
        return self.positive_sentences


# for testing DataLoader
if __name__ == '__main__':
    d = DataLoader()
    print(len(d.get_negative_sents()))
    print(len(d.get_positive_sents()))
