import nltk
from nltk import word_tokenize
from Parser import SentParser
from Lexica import DataLoader
from typing import List, Tuple, Dict, Any
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
        self.false_positive = 0
        self.true_negative = 0
        self.false_negative = 0
        self.true_neutral = 0
        self.false_neutral = 0

    def part_of_speech_tagging(self, words: List[str]) -> List[Tuple[str, str]]:
        """
        perform part-of-speech tagging
        :param words: a list of words
        """
        normal_pos_tag = nltk.pos_tag(words[:-1])   # omit the last period
        return normal_pos_tag

    def parse_and_sentify(self, token_list: List[str]) -> Tuple[List[Tuple[Any, int]], Dict[str, str]]:
        """
        parse the sentence
        :param token_list: tokens of a sentence
        :return return the most possible sentiment
        """
        # retrieve sentiment labels of all possible parse trees
        sentiments, parse_trees = self.parser.parse(token_list[:-1]) # omit the last period
        # return the most probable sentiment
        return Counter(sentiments).most_common(), parse_trees

    def run_pipeline(self) -> None:
        """
        run the sentiment pipeline
        """
        try:
            # clear the previous result files
            self.parser.clear_directory()
            # tokenization + pos tagging
            # positive sentences
            for pos_sent in self.lexica.get_positive_sents():
                words = word_tokenize(pos_sent)
                pos = self.part_of_speech_tagging(words)
                # print('part-of-speech:', pos)
                print('analyzing sentence:', pos_sent)
                senti, trees = self.parse_and_sentify(words)
                # write the sentencee and the ground-truth and the prediction to a result file
                self.output_results(pos_sent, 'positive', senti, trees)
            # negative sentences
            for neg_sent in self.lexica.get_negative_sents():
                words = word_tokenize(neg_sent)
                pos = self.part_of_speech_tagging(words)
                # print('part-of-speech:', pos)
                print('analyzing sentence:', neg_sent)
                senti, trees = self.parse_and_sentify(words)
                # write the ground-truth and prediction to a result file
                self.output_results(neg_sent, 'negative', senti, trees)
            # neutral sentences
            for neu_sent in self.lexica.get_neutral_sents():
                words = word_tokenize(neu_sent)
                pos = self.part_of_speech_tagging(words)
                # print('part-of-speech:', pos)
                print('analyzing sentence:', neu_sent)
                senti, trees = self.parse_and_sentify(words)
                # write the ground-truth and prediction to a result file
                self.output_results(neu_sent, 'neutral', senti, trees)
        except Exception as ex:
            print(ex.args[0])

    def output_results(self, sentence: str, ground_truth: str, labels: List[Tuple[Any, int]], trees: Dict[str, str]) -> None:
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
        if ground_truth in [label[0] for label in labels]:
            # write the sentence and the ground_truth and label to Good.txt
            with open("saved_results/Good.txt", "a+") as writer:
                # write the input sentence
                writer.write(sentence + '\r\n')
                # write the ground-truth label
                writer.write(ground_truth + '\t|\t')
                # write the prediction labels
                writer.write('[')
                for i in range(len(labels)-1):
                    writer.write(labels[i][0] + ', ')
                writer.write(labels[-1][0] + ']')
                writer.write('\r\n\r\n')
                # write the first tree with prediction label that has the most votes
                for label in labels:
                    writer.write(trees[label[0]][0])
                    writer.write('\r\n')
                writer.write('-------------------------------------------------------------------\r\n')
            # record performance
            if ground_truth == 'negative':
                self.true_negative += 1
            elif ground_truth == 'positive':
                self.true_positive += 1
            elif ground_truth == 'neutral':
                self.true_neutral += 1
        else:
            # write the sentence and the ground_truth and label to False.txt
            with open("saved_results/False.txt", "a+") as writer:
                # write the input sentence
                writer.write(sentence + '\r\n')
                # write the ground-truth label
                writer.write(ground_truth + '\t|\t')
                # write the prediction labels
                writer.write('[')
                for i in range(len(labels) - 1):
                    writer.write(labels[i][0] + ', ')
                writer.write(labels[-1][0] + ']')
                writer.write('\r\n\r\n')
                # write the first tree with prediction label that has the most votes
                for label in labels:
                    writer.write(trees[label[0]][0])
                    writer.write('\r\n')
                writer.write('-------------------------------------------------------------------\r\n')
            # record performance
            if 'negative' in labels:
                self.false_negative += 1
            if 'positive' in labels:
                self.false_positive += 1
            if 'neutral' in labels:
                self.false_neutral += 1

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
