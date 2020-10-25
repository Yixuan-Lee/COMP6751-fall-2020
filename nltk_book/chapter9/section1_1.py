"""
simple CFG in (5):

    S   ->   NP VP
    NP  ->   Det N
    VP  ->   V

    Det  ->  'this'
    N    ->  'dog'
    V    ->  'runs

(5) grammars does not block unwanted sequence such as:
    "this dogs run"
    "these dog runs"

So, one solution is to add new non-terminals and productions to the grammar
grammar (6):
    S -> NP_SG VP_SG
    S -> NP_PL VP_PL
    NP_SG -> Det_SG N_SG
    NP_PL -> Det_PL N_PL
    VP_SG -> V_SG
    VP_PL -> V_PL

    Det_SG -> 'this'
    Det_PL -> 'these'
    N_SG -> 'dog'
    N_PL -> 'dogs'
    V_SG -> 'runs'
    V_PL -> 'run'

in grammar (6), a pair of productions (e.g. NP_SG, NP_PL) correspond to one production in grammar (5)
    NP_SG covers the sentences involving singular subject NPs and VPs
    NP_PL covers sentences with plural subject NPs and VPs

Issues of grammar (6):
    1. with a larger grammar that covers a reasonable subset of English constructions, the prospect of doubling the grammar size is very unattractive.
    2. if we consider:
        a. first person agreement
        b. second person agreement
        c. third person agreement
       for both
        aa. singular
        bb. pluriel
       our original grammar rules would expand by a factor of 6
Solution:
    use attributes and constraints
    (see next section)

"""