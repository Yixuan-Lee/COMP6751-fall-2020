import nltk

# 2. define a simple chunk grammar consisting of two rules:
#    1) match an optional determiner or (|) possessive pronoun, zero or more adjective, then a noun
#    2) match one or more proper nouns (+)
# $ in regular expressions must be backslash escaped
grammar = r"""
    NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
        {<NNP>+}                # chunk sequences of proper nouns
"""
cp = nltk.RegexpParser(grammar)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
result = cp.parse(sentence)
print(result)
# result.draw()
print('--------------------------------------------------')

# if overlap, then the leftmost match takes precedence
nouns = [("money", "NN"), ("market", "NN"), ("fund", "NN")]
# grammar = "NP: {<NN><NN>}  # Chunk two consecutive nouns"     # with issue
grammar = "NP: {<NN>+}"     # avoid the issue
cp = nltk.RegexpParser(grammar)
result = cp.parse(nouns)
print(result)
result.draw()

