"""
Reference:
https://www.nltk.org/api/nltk.sentiment.html

"""

import nltk
from nltk.sentiment.util import demo_sent_subjectivity

# nltk.download('subjectivity')

if __name__ == '__main__':
    demo_sent_subjectivity("it's a compelling story .")
    # demo_sent_subjectivity("it has low impact but it's a compelling story .")
    # demo_sent_subjectivity("it has gut-wrenching impact and it is a compelling story .")
    # demo_sent_subjectivity("this does not have gut-wrenching impact but it's a compelling story .")
    # demo_sent_subjectivity("this compelling story with gut-wrenching impact .")
    # demo_sent_subjectivity("this may not have the dramatic gut-wrenching impact of other holocaust films , but it's a compelling story , mainly because of the way it's told by the people who were there .")
    # demo_sent_subjectivity("a perfect example .")
    # demo_sent_subjectivity("well-intentioned movie making .")

    print('===============')

    # demo_liu_hu_lexicon("it's a compelling story , but it has low impact .")
    # demo_liu_hu_lexicon("manipulative movie making .")
    # demo_liu_hu_lexicon("shamelessly manipulative movie making .")
    # demo_liu_hu_lexicon("well-intentioned but manipulative movie making .")
    # demo_liu_hu_lexicon("a perfect example of well-intentioned but manipulative movie making .")
    # demo_liu_hu_lexicon("a perfect example of rancid , well-intentioned , but shamelessly manipulative movie making .")
