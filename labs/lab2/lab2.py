import nltk
from nltk import word_tokenize

# ### Lab 2 task 1: Manually assign POS tags for the following sentence:
# text = word_tokenize("They wind back the clock, while we chase after the wind.")
# print(nltk.pos_tag(text))   # output: [('They', 'PRP'), ('wind', 'VBP'), ('back', 'RB'), ('the', 'DT'), ('clock', 'NN'), (',', ','), ('while', 'IN'), ('we', 'PRP'), ('chase', 'VBP'), ('after', 'IN'), ('the', 'DT'), ('wind', 'NN'), ('.', '.')]
# print(nltk.pos_tag(text, tagset='universal'))

print('--------------------------------------------------------------------')

# ### Lab 2 task 2: Create a dictionary e, to represent a single lexical entry for put.


print('--------------------------------------------------------------------')


# ### Lab 2 task 3: write a CFG fragment that deals properly with the following

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> IV | TV NP | DatV NP PP | SV Adj | SV S
  PP -> P NP
  IV -> "barked"
  TV -> "put" | "puts" | "saw"
  DatV -> "gave"
  SV -> "said"
  NP -> "Joe" | Det N | Det N PP
  Det -> "a" | "an" | "the"
  N -> "man" | "fish" | "log"
  P -> "on" | "with"
  """)
a = "Joe put on the log".split()
b = "Joe put the fish on log".split()
c = "Joe really put the fish on the log".split()
d = "Joe never puts fish on logs".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(c):
    print(tree)
