import nltk
from typing import List
from collections import defaultdict

class UnitEntityDetector:
    def __init__(self, pos_taggings: List[List[str]]):
        self.pos_tags = pos_taggings
        self.unit_entities: List[str] = list()

    def unit_detection(self) -> List[str]:
        unit_chunker_grammar = r"""
            UN: {<CD> <NNS> <IN> <NN>}          # E.g. 3 meters of water, 2 miles per hour
                {<CD> <JJ> <JJ> <NNS> <IN> <NN>}    # E.g. 1 actual cubic centimeters per minute
                {<CD> <JJ> <NN> <NN>}           # E.g. 1 atomic mass unit, 1 British shipping ton
                {<CD> <JJ> <JJ> <NN>}           # E.g. 1 modified Julian NN
                {<CD> <JJ> <NN>}                # E.g. 1 square meter, 3 cubic inch
                {<CD> <JJ> <NNS>}               # E.g. 6 astronomical units
                {<CD> <JJ> <NNP>}               # E.g. 1 alpha TE
                {<CD> <VBG> <JJ> <NN>}          # E.g. 1 cooling degree day
                {<CD> <NN> <JJ> <NN>}           # E.g. 1 bank cubic meter
                {<CD> <NN> <VBG> <NN>}          # E.g. 1 color rendering index
                {<CD> <NN> <NN> <NN>}           # E.g. 1 blood alcohol level, 1 body mass index
                {<CD> <NN> <NN>}                # E.g. 1 mach number, 1 absorbance unit
                {<CD> <NN> <IN> <NN> <NN>}      # E.g. 1 gallon of gasoline equivalent
                {<CD> <NN> <IN> <NN>}           # E.g. 1 bit per second, 1 foot of head
                {<CD> <NN> <IN>}                # E.g. 1 ac in
                {<CD> <NN> <NNP>}               # E.g. 1 cm Hg
                {<CD> <NN>}                     # E.g. 1 mile
                {<CD> <FW> <FW>}                # E.g. 1 caballo de vapor
                {<CD> <NNP> <NN> <NNP>}         # E.g. 2 Celsius heat units
                {<CD> <NNP> <NN> <NN>}          # E.g. 1 Celsius heat unit
                {<CD> <NNP> <NN>}               # E.g. 20 admiralty mile
                {<CD> <CD>}                     # E.g. 328 billion
                {<CD> <NNP>}                    # E.g. 2000 AD
                {<CD> <NNS>}                    # E.g. 2 miles, 3 meters
                {<CD> <IN>}                     # E.g. 1 as, 1 at
                {<CD> <$>}                      # E.g. 1 $
        """
        cp = nltk.RegexpParser(unit_chunker_grammar)

        # read from unit_gazetteer
        gazetteer = defaultdict(set)
        with open("unit_gazetteer.txt", "r") as f:
            for line in f:
                pos, word = line.split()
                gazetteer[pos].add(word)
        # print(gazetteer)

        for i in range(len(self.pos_tags)):
            tree = cp.parse(self.pos_tags[i])
            for subtree in tree.subtrees():
                if subtree.label() == 'UN':
                    tup_list = subtree.leaves()
                    tup_units = tup_list[1:]

                    # check if all words in tup_units exist in gazetteer
                    in_gazetteer = True
                    for tup in tup_units:
                        # tup[0]: token
                        # tup[1]: tag
                        if tup[0] not in gazetteer[tup[1]]:
                            # one of the words is not un unit gazetteer
                            in_gazetteer = False
                            break
                    # if yes, then add the unit entity to the list
                    if in_gazetteer is True:
                        self.unit_entities.append(' '.join(word[0] for word in subtree.leaves()))

        return self.unit_entities
