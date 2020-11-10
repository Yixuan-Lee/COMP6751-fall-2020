import nltk
from nltk import word_tokenize
from Parser import SentParser
from Lexica import DataLoader
from typing import List, Tuple
from collections import Counter


class SentimentPipeline:
    def __init__(self, parser: SentParser, lexica: DataLoader):
        """
        constructor
        :param parser: Earley parser
        :param lexica: Lexica data loader
        """
        self.parser = parser
        self.lexica = lexica
        self.true_positive = 0
        self.true_negative = 0
        self.false_positive = 0
        self.false_negative = 0

    def part_of_speech_tagging(self, words: List[str]) -> List[Tuple[str, str]]:
        """
        perform part-of-speech tagging
        :param words: a list of words
        """
        normal_pos_tag = nltk.pos_tag(words[:-1])   # omit the last period
        return normal_pos_tag

    def parse_and_sentify(self, token_list: List[str]) -> str:
        """
        parse the sentence
        :param token_list: tokens of a sentence
        :return return the most possible sentiment
        """
        self.parser.clear_directory()
        # retrieve sentiment labels of all possible parse trees
        sentiments = self.parser.parse(token_list)
        if len(sentiments) == 0:
            # meaning the parser doesn't have the corresponding gramar for the sentence
            return 'unknown'
        else:
            # return the most probable sentiment
            return Counter(sentiments).most_common()[0][0]

    def run_pipeline(self) -> None:
        """
        run the sentiment pipeline
        """
        try:
            # tokenization + pos tagging
            # positive sentences
            for pos_sent in self.lexica.get_positive_sents():
                words = word_tokenize(pos_sent)
                pos = self.part_of_speech_tagging(words)
                senti = self.parse_and_sentify(words)
                # write the sentencee and the ground-truth and the prediction to a result file
                self.output_results(pos_sent, 'positive', senti)
            # negative sentences
            for neg_sent in self.lexica.get_negative_sents():
                words = word_tokenize(neg_sent)
                pos = self.part_of_speech_tagging(words)
                senti = self.parse_and_sentify(words)
                # write the ground-truth and prediction to a result file
                self.output_results(neg_sent, 'negative', senti)
        except Exception as ex:
            print(ex.args[0])

    def output_results(self, sentence: str, ground_truth: str, label: str) -> None:
        """
        write the result with the following format
            sentence1
            ground_truth label  prediction label
            sentence 2
            ground_truth label  prediction label
            ...
        :param sentence: sentence
        :param ground_truth: ground-truth label
        :param label: prediction label
        """
        if ground_truth == label:
            # write the sentence and the ground_truth and label to Good.txt
            with open("Good.txt", "a+") as writer:
                writer.write(sentence)
                writer.write(ground_truth + '\t' + label)
            if ground_truth == 'negative':
                self.true_negative += 1
            elif ground_truth == 'positive':
                self.true_positive += 1
        else:
            # write the sentence and the ground_truth and label to False.txt
            with open("False.txt", "a+") as writer:
                writer.write(sentence)
                writer.write(ground_truth + '\t' + label)
            if label == 'negative':
                self.false_negative += 1
            elif label == 'positive':
                self.false_positive += 1

    def performance(self) -> None:
        recall = self.true_positive / (self.true_positive + self.false_negative)
        precision = self.true_positive / (self.true_positive + self.false_positive)
        f1_score = (precision * recall) / (precision + recall)
        print('True Negative =', self.true_negative)
        print('True Positive =', self.true_positive)
        print('False Negative =', self.false_negative)
        print('False Positive =', self.false_negative)
        print('Precision =', precision)
        print('Recall =', recall)
        print('F1 measure =', f1_score)

    def print_lexica(self):
        print('positive sentences:')
        for sent in self.lexica.get_positive_sents():
            print(sent)
        print()
        print('negative sentences:')
        for sent in self.lexica.get_negative_sents():
            print(sent)
