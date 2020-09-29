import nltk

sent = "Indonesia is unlikely to import copra from the Philippines in 1987."
sents = nltk.sent_tokenize(sent)
for s in sents:
    words = nltk.word_tokenize(s)
    pos_tag = nltk.pos_tag(words)

    print(words)
    print(pos_tag)
    print('-----------------------------------')


'''
cd nn
cd nn nns
'''