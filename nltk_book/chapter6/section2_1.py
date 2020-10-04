"""
Chapter 6 section 2.1 Sentence Segmentation

website: http://www.nltk.org/book/ch06.html#sec-further-examples-of-supervised-classification

"""

import nltk

# Sentence segmentation can be viewed as a classification task whenever we
# encounter a symbol, we need to decide whether it terminates the preceeding
# sentence
print('--------------------- a. ------------------------')
sents = nltk.corpus.treebank_raw.sents()
print(sents)
tokens = []
boundaries = set()
offset = 0
for sent in sents:
    tokens.extend(sent)
    offset += len(sent)
    boundaries.add(offset - 1)
print(tokens)

def punct_features(tokens, i):
    return {'next-word-capitalized': tokens[i+1][0].isupper() if i+1 < len(tokens) else True,
            'prev-word': tokens[i - 1].lower(),
            'punct': tokens[i],
            'prev-word-is-one-char': len(tokens[i - 1]) == 1}

# ## create a list of labeled featuresets by selecting all the punctuation
# ## tokens, and tagging whether they are boundary tokens or not
featuresets = [(punct_features(tokens, i), (i in boundaries))
                for i in range(1, len(tokens)-1)
                if tokens[i] in '.?!']

# ## use featureset, train and evauate a punctutaion classifier
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]    # split train/test set
classifier = nltk.NaiveBayesClassifier.train(train_set)
print('accuracy:', nltk.classify.accuracy(classifier, test_set))

# ## use the classifier to perform sentence segmentation
print('--------------------- b. ------------------------')
def segment_sentences(words):
    start = 0
    sents = []
    for i, word in enumerate(words):
        if word in '.?!' and classifier.classify(punct_features(words, i)) == True:
            sents.append(words[start:i+1])
            start = i+1
    if start < len(words):
        sents.append(words[start:])
    return sents

# ## test segment_sentences function
# ## test-case-1: reuter training/267
from nltk.corpus import reuters
words = reuters.words('training/267')
print(words)
print(len(words))
print(words[-10:])
sents = segment_sentences(words)
print(sents)
print(len(sents))
print('------------------------------------------')
# ## test-case-2: a text snippet copied from web
my_sent = "In English-speaking countries (except South Africa), in Mexico and in most Asian countries the period (.) is used as the decimal marker (decimal point) to separate the whole number and fractional portions of a number. In continental Europe and most South American countries the decimal marker is the comma (,). The International System (SI) allows either the period or the comma to be used; the Dictionary uses the period. Wikipedia's decimal separator article has a lists of countries using each marker."
from nltk import word_tokenize
tokens = word_tokenize(my_sent)
print(tokens)
print(len(tokens))
sents = segment_sentences(tokens)
print(sents)
print(len(sents))

