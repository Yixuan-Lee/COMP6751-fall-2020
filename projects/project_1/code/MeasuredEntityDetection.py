import nltk
from typing import List
from collections import defaultdict

class UnitEntityDetector:
    def __init__(self, pos_taggings: List[List[str]]):
        self.pos_tags = pos_taggings
        self.unit_entities: List[str] = list()

    def unit_detection(self) -> List[str]:
        unit_chunker_grammar = r"""
            UN: {<CD> <NNS> <IN> <NN>}  # E.g. 3 meters of water, 2 miles per hour
                {<CD> <JJ> <NN>}        # E.g. 1 square meter, 3 cubic inch
                {<CD> <JJ> <NNS>}       # E.g. 6 astronomical units
                {<CD> <NN> <NN>}        # E.g. 1 mach number
                {<CD> <NN>}             # E.g. 1 mile
                {<CD> <NNS>}            # E.g. 2 miles, 3 meters
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
                            in_gazetteer = False
                    # if yes, then add the unit entity to the list
                    if in_gazetteer is True:
                        self.unit_entities.append(' '.join(word[0] for word in subtree.leaves()))

        return self.unit_entities
