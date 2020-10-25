"""
tutorial website: https://www.nltk.org/book/ch09.html
"""

if __name__ == '__main__':
    # CAT: grammatical category
    # ORTH: orthography 拼写
    # REF: reference of kim
    # REL: relation expressed by chase
    kim = {'CAT': 'NP',
           'ORTH': 'Kim',
           'REF': 'k'}
    chase = {'CAT': 'V',
             'ORTH': 'chased',
             'REL': 'chase'}
    # add two features (semantic role) for chase
    # AGT: agent (subject)
    # PAT: patient (object)
    chase['AGT'] = 'sbj'    # agent placeholder (subject, chase的执行者)
    chase['PAT'] = 'obj'    # patient placeholder (object, chase的作用对象)

    # process a sentence
    sent = 'Kim chased Lee'
    tokens = sent.split()
    # add a feature structure
    lee = {'CAT': 'NP', 'ORTH': 'Lee', 'REF': 'l'}
    def lex2fs(word):
        for fs in [kim, lee, chase]:
            if fs['ORTH'] == word:
                return fs
    subj, verb, obj = lex2fs(tokens[0]), lex2fs(tokens[1]), lex2fs(tokens[2])
    verb['AGT'] = subj['REF']
    verb['PAT'] = obj['REF']
    for k in ['ORTH', 'REL', 'AGT', 'PAT']:
        print("%-5s => %s" % (k, verb[k]))
        
