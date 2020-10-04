import nltk

# define a chunk grammar
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

# 2. define a simple grammar with a single regular-expression rule:
# NP chunk should be formed whenever the chunker finds an optional (?) determiner (DT) followed by any number (*) of adjectives (JJ) and then a noun (NN)
grammar = "NP: {<DT>?<JJ>*<NN>}"

# 3. use the grammar to create a chunk parser
cp = nltk.RegexpParser(grammar)

# 4. test it on example sentence
result = cp.parse(sentence)

# 5. print the result
print(result)

# 6. display the tree graphically
# result.draw()


