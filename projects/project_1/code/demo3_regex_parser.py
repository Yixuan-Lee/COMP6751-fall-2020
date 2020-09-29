import nltk

sents = '''
foot
inches
metre
yard
feet
mile
yards
kilometres
square inch
centimetres
square foot
decimetres
square yard
acre
hectare
square mile
hectares
cubic inch
cubic foot
cubic yard
pint
oz
quart
pints
litres
gallons
quarts
peck
grams
ounce
drams
grains
kilogram
stone
decametre
hectometres
grains
grain
ton
bag
bale
bottle
box
dozen
package
packages
piece
pieces
sheet
unit
system of units
meter
degree
Celsius
Fahrenheit
newton
kilopound
square meter
square millimeter
volt
ohm
hour
minute
minutes
second
seconds
army
pack
throng
brood
hive
school
swarm
team
field
bar
stack
'''
lib = sents.split('\n')[1:-1]

lib_words = []
for l in lib:
    if l.find(' ') == -1:
        lib_words.append(l)
    else:
        lib_words.extend(l.split(' '))
print(lib_words)

sentences = nltk.sent_tokenize(sents)


grammar = r"""
    UN: {<CD> <NNS>}
        {<CD> <NN> <NN>}
        {<CD> <NNS> <IN> <NN>}
"""
cp = nltk.RegexpParser(grammar)

for s in sentences:
    words = nltk.word_tokenize(s)
    pos_tags = nltk.pos_tag(words)
    print(pos_tags)
    tree = cp.parse(pos_tags)
    # print(tree)
    # tree.draw()

    # for subtree in tree.subtrees():
    #     if subtree.label() == 'UN':
    #         for leaf in subtree.leaves():
    #             if leaf in lib_words:
    #                 print(leaf)



