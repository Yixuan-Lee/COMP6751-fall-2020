"""
Reference:
https://finnaarupnielsen.wordpress.com/2011/06/20/simplest-sentiment-analysis-in-python-with-af/

"""

# !/usr/bin/python
#
# (originally entered at https://gist.github.com/1035399)
#
# License: GPLv3
#
# To download the AFINN word list do:
# wget http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6010/zip/imm6010.zip
# unzip imm6010.zip
#
# Note that for pedagogic reasons there is a UNICODE/UTF-8 error in the code.

import math
import re
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

class SSAP:
    def __init__(self):
        # AFINN-111 is as of June 2011 the most recent version of AFINN
        filenameAFINN = 'AFINN/AFINN-111.txt'
        # afinn = dict(map(lambda w, s: (w, int(s)), [ws.strip().split('\t') for ws in open(filenameAFINN)])) # python 2
        self.afinn = dict(map(lambda ws: (ws[0], int(ws[1])), [ws.strip().split('\t') for ws in open(filenameAFINN)]))  # python 3
        # Word splitter pattern
        self.pattern_split = re.compile(r"\W+")

        # performance
        self.true_positive = 0
        self.false_positive = 0
        self.true_negative = 0
        self.false_negative = 0
        self.true_neutral = 0
        self.false_neutral = 0

    def sentiment(self, text):
        """
        Returns a float for sentiment strength based on the input text.
        Positive values are positive valence, negative value are negative valence.
        """
        words = self.pattern_split.split(text.lower())
        # sentiments = map(lambda word: afinn.get(word, 0), words)    # python 2
        sentiments = list(map(lambda word: self.afinn.get(word, 0), words))  # python 3
        if sentiments:
            # How should you weight the individual word sentiments?
            # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
            sentiment = float(sum(sentiments)) / math.sqrt(len(sentiments))
        else:
            sentiment = 0
        return sentiment

    def predict(self, text: str, ground_truth: str):
        sentiment_score = self.sentiment(text)
        if ground_truth == 'positive':
            if sentiment_score > 0:
                self.true_positive += 1
            elif sentiment_score == 0:
                self.false_neutral += 1
            elif sentiment_score < 0:
                self.false_negative += 1
        elif ground_truth == 'neutral':
            if sentiment_score > 0:
                self.false_positive += 1
            elif sentiment_score == 0:
                self.true_neutral += 1
            elif sentiment_score < 0:
                self.false_negative += 1
        elif ground_truth == 'negative':
            if sentiment_score > 0:
                self.false_positive += 1
            elif sentiment_score == 0:
                self.false_neutral += 1
            elif sentiment_score < 0:
                self.true_negative += 1

    def performance(self):
        recall = self.true_positive / (self.true_positive + self.false_negative)
        precision = self.true_positive / (self.true_positive + self.false_positive)
        f1_score = (precision * recall) / (precision + recall)
        print('True Negative =', self.true_negative)
        print('True Neutral =', self.true_neutral)
        print('True Positive =', self.true_positive)
        print('False Negative =', self.false_negative)
        print('False Neutral =', self.false_neutral)
        print('False Positive =', self.false_negative)
        print('Precision =', precision)
        print('Recall =', recall)
        print('F1 measure =', f1_score)


# testing SSAP baseline
# if __name__ == '__main__':
#     # Single sentence example:
#     text = "Finn is stupid and idiotic"
#     print("%6.2f %s" % (sentiment(text), text))
#
#     # No negation and booster words handled in this approach
#     text = "Finn is only a tiny bit stupid and not idiotic"
#     print("%6.2f %s" % (sentiment(text), text))
