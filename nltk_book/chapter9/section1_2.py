"""
a noun has the property of being plural:
    N[NUM=pl]

productions in grammar (6):
    Det_SG -> 'this'
    Det_PL -> 'these'
    N_SG -> 'dog'
    N_PL -> 'dogs'
    V_SG -> 'runs'
    V_PL -> 'run'
since category N has a grammartical feature called NUM,
the productions above can be replaced by NUM feature:
    Det[NUM=sg] -> 'this'
    Det[NUM=pl] -> 'these'
    N[NUM=sg] -> 'dog'
    N[NUM=pl] -> 'dogs'
    V[NUM=sg] -> 'runs'
    V[NUM=pl] -> 'run'
It seems like not help too much, but we can add variables over feature values
and use variables to state constraints:
    S -> NP[NUM=?n] VP[NUM=?n]
    NP[NUM=?n] -> Det[NUM=?n] N[NUM=?n]
    VP[NUM=?n] -> V[NUM=?n]

?n as a variable over values of NUM, it can be instantiated either to sg or pl, within a given production.



"""

import nltk
# nltk.download('book_grammars')
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
print('-------------------------------------------------')

tokens = 'Kim likes children'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
for tree in cp.parse(tokens):
    print(tree)
