"""
1. More attributes

In addition to attributes TENSE, NUM, we can still specify a boolean property
which indicates the type of word which the current word can receive.
For example:
    V[TENSE=pres, +AUX] -> 'can'
    V[TENSE=pres, +AUX] -> 'may'

    V[TENSE=pres, -AUX] -> 'walks'
    V[TENSE=pres, -AUX] -> 'likes'

V[TENSE=pres, +AUX] means 'can' and 'may' can receives the value pres for TENSE
and +/true for AUX. Since 'walks' and 'likes' have AUX with -/false, so they
cannot add after 'can' and 'may'.


2. Add more complex attributes

We can group together agreement features, such as person (PER), number (NUM),
gender (GND) etc. asa distinguished part of a category.
Usually, we group them as the value of AGR (Attribute Group Rendering)
For example:
    [POS = N           ]
    [                  ]
    [AGR = [PER = 3   ]]
    [      [NUM = pl  ]]
    [      [GND = fem ]]
In terms of grammar productions, it can be like:
    S                    -> NP[AGR=?n] VP[AGR=?n]
    NP[AGR=?n]           -> PropN[AGR=?n]
    VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj

    Cop[TENSE=pres,  AGR=[NUM=sg, PER=3]] -> 'is'
    PropN[AGR=[NUM=sg, PER=3]]            -> 'Kim'
    Adj                                   -> 'happy'

"""
