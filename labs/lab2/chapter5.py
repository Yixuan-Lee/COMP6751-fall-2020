"""
NLTK book Chapter 5: Categorizing and Tagging Words

Website: http://www.nltk.org/book/ch05.html

"""

import nltk
from nltk import word_tokenize

# #################### 1. Using a Tagger #################### #
# includes:
#       1. part-of-speech tagging (POS tagging)
#       2. search words with similar context

# 1.1 part-of-speech tagging
# Note:
#   tagset (refer to slide week1 - page 23)
#   CC: coordinating conjunction
#   RB: adverb
#   IN: preposition/subordinate conjunction
#   NN: singular noun
#   RB: adverb
#   JJ: adjective
#   etc.
## nltk.download('averaged_perceptron_tagger')
# text = word_tokenize("And now for something completely different")
# print(nltk.pos_tag(text))   # output: [('And', 'CC'), ('now', 'RB'), ('for', 'IN'), ('something', 'NN'), ('completely', 'RB'), ('different', 'JJ')]
# text = word_tokenize("They refuse to permit us to obtain the refuse permit")
# print(nltk.pos_tag(text))   # output: [('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'), ('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN')]

# # find the words that appear in the same context as 'woman', 'bought', 'over', 'the'
# text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
# text.similar('woman')
# text.similar('bought')
# text.similar('over')
# text.similar('the')

# #################### 1. Tagged Corpora #################### #
# includes:
#       1. str2tuple(.) to display tagged tokens
#       2. tagged_words() to read tagged corpora

# # 2.1 representing tagged tokens
# tagged_token = nltk.tag.str2tuple('fly/NN')
# print(tagged_token)
# print(tagged_token[0])
# print(tagged_token[1])

# sent = '''
# The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
# other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
# Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
# said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
# accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
# interest/NN of/IN both/ABX governments/NNS ''/'' ./.
# '''
# print([nltk.tag.str2tuple(t) for t in sent.split()])

# # 2.2 reading tagged corpora
## nltk.download('brown')
# print(nltk.corpus.brown.tagged_words())
## nltk.download('universal_tagset')
# print(nltk.corpus.brown.tagged_words(tagset='universal'))
## nltk.download('nps_chat')
# print(nltk.corpus.nps_chat.tagged_words())
## nltk.download('treebank')
# print(nltk.corpus.treebank.tagged_words())

# # use different tagset on tagged corpora
# print(nltk.corpus.brown.tagged_words(tagset='universal'))
# print(nltk.corpus.treebank.tagged_words(tagset='universal'))

# # tagged corpora for various language in NLTK
## nltk.download('sinica_treebank')
# print(nltk.corpus.sinica_treebank.tagged_words())

# # 2.3 a universal part-of-speech tagset
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.most_common())

# # 2.4 nouns
word_tag_pairs = nltk.bigrams(brown_news_tagged)
noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']
fdist = nltk.FreqDist(noun_preceders)
print([tag for (tag, _) in fdist.most_common()])

# # 2.5 verbs
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
print([wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'])

cfd1 = nltk.ConditionalFreqDist(wsj)
print(cfd1['yield'].most_common())
print(cfd1['cut'].most_common())




