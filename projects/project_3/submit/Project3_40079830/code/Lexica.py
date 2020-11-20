import os
from typing import List


class DataLoader:
    def __init__(self):
        """
        constructor
        """
        self.positive_sentences = []
        self.negative_sentences = []
        self.neutral_sentences = []

        # response = input('Are you going to use default testing files? (Y/N) ')
        response = "Yes"
        if response.lower() == 'y' or response.lower() == 'yes':
            positive_filepath = 'data/positive.txt'
            negative_filepath = 'data/negative.txt'
            neutral_filepath = 'data/neutral.txt'
        else:
            positive_filepath = input('Input your file path containing positive sentences: ')
            negative_filepath = input('Input your file path containing negative sentences: ')
            neutral_filepath = input('Input your file path containing neutral sentences: ')
        print('positive file path:', positive_filepath)
        print('negative file path:', negative_filepath)
        print('neutral file path:', neutral_filepath)
        print()

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

        # read neutral sentences
        if os.path.exists(neutral_filepath):
            with open(neutral_filepath, "r") as reader:
                self.neutral_sentences = reader.readlines()
            self.neutral_sentences = [sent.rstrip() for sent in self.neutral_sentences]
        else:
            print(neutral_filepath + ' does not exist on local.')

    def get_negative_sents(self) -> List[str]:
        return self.negative_sentences

    def get_positive_sents(self) -> List[str]:
        return self.positive_sentences

    def get_neutral_sents(self) -> List[str]:
        return self.neutral_sentences


# # for testing DataLoader
# if __name__ == '__main__':
#     d = DataLoader()
#     print(len(d.get_negative_sents()))
#     print(len(d.get_positive_sents()))
