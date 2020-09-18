# Lab Assignment 1

if __name__ == "__main__":
    # 1. install NLTK3
    # (done)
    import nltk

# ---------------------------------------------------------------------------

    # 2. download the reuters corpus in NLTK
    # nltk.download('reuters')  # download reuters corpus
    # nltk.download('punkt')    # download english tokenizer
    from nltk.corpus import reuters

# ---------------------------------------------------------------------------

    # 3. In the Reuters corpus
    # the number of documents
    # print(len(reuters.fileids()))   # 10788

    # the number of words
    # print(len(reuters.words()))     # 1720901

    # the number of sentences
    # print(len(reuters.sents()))     # 54716

# ---------------------------------------------------------------------------

    # 4. For the text with fileid 'training/9920', determine
    # the number of words
    # print(len(reuters.words(fileids=['training/9920'])))  # 71

    # the number of single word prepositions
    # need to consider lower and upper cases
    single_word_prepositions = ['about', 'beside', 'near', 'to', 'above', 'between', 'of', 'towards', 'across', 'beyond', 'off', 'under', 'after', 'by', 'on', 'underneath', 'against', 'despite', 'onto', 'unlike', 'along', 'down', 'opposite', 'until', 'among', 'during', 'out', 'up', 'around', 'except', 'outside', 'upon', 'as', 'for', 'over', 'via', 'at', 'from', 'past', 'with', 'before', 'in', 'round', 'within', 'behind', 'inside', 'since', 'without', 'below', 'into', 'than', 'beneath', 'like', 'through']
    count = 0
    for w in reuters.words(fileids=['training/9920']):
        if w.lower() in single_word_prepositions:
            count += 1
    print(count)    # 9

# ---------------------------------------------------------------------------

    # 5. create a table that lists fileIDs for each of 90 categories
    # categories = reuters.categories()   # get 90 categories
    # fileids = []
    # for category in categories:
    #     fileids.append(reuters.fileids([category]))
    # # print(fileids)


# ---------------------------------------------------------------------------

    # 6. write a function word_freq that takes a word and a fileID, and
    # compute the frequency of the word in that file
    # def word_freq(word, fileId) -> int:
    #     count = 0
    #     words = reuters.words(fileids=[fileId])
    #     for w in words:
    #         if w == word:
    #             count += 1
    #     return count
    # print(word_freq('said', 'training/9920'))   # 2

# ---------------------------------------------------------------------------

    # 7.1 inspect the files: is a file equal to a newspaper article?
    # answer: no, there are some markers, annotations in some files

    # 7.2 inspect a newspaper article (9920). Are all the character part of
    # the printed article?
    # answer: no, characters like "CONTEL &lt;CTC>" don't belong to the body

    # 7.3 begin data pre-processing (or cleaning)
    # Q1: What is the data that is not part of the printed article?

    # Q2: Why is it there?

    # Q3: Can you extract the original printed text?

    # Q4: Can you do it without losing the extra information?

    # Q5: What could that be used for?


# ---------------------------------------------------------------------------
