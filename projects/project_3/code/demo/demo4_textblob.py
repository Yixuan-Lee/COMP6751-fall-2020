"""
Reference:
https://stackoverflow.com/questions/34190860/sentiment-analysis-for-sentences-positive-negative-and-neutral

"""

from textblob import TextBlob

text = '''
These laptops are horrible but I've seen worse. How about lunch today? The food was okay.
'''

blob = TextBlob(text)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
