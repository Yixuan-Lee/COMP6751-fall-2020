import nltk
from typing import List
from collections import defaultdict

class UnitEntityDetector:
    def __init__(self, pos_taggings: List[List[str]]):
        self.pos_tags = pos_taggings
        self.unit_entities: List[str] = list()

    def unit_detection(self) -> List[str]:
        unit_chunker_grammar = r"""
            UN: {<CD> <NN> <IN|JJ|VBG|NNP> <NN>{0,2}}   # E.g. 1 ac in, 1 bit per second, 1 foot of head, 1 gallon of gasoline equivalent, 1 bank cubic meter, 1 color rendering index, 1 cm Hg
                {<CD> <NN> <FW> <FW>}                   # E.g. 1 caballo de vapor
                {<CD> <NN|NNP> <NN>? <NN|NNP|NNS>?}     # E.g. 2 Celsius heat units, 1 Celsius heat unit, 20 admiralty mile, 2000 AD
                {<CD> <NN>{1,3}}                        # E.g. 1 blood alcohol level, 1 body mass index, 1 mach number, 1 absorbance unit, 1 mile  
                {<CD> <NNS> <IN> <NN>}                  # E.g. 3 meters of water, 2 miles per hour
                {<CD> <CD>? <NNS>}                            # E.g. two countries, 2 miles, 3 meters, 2 mln tonnes
                {<CD> <JJ> <NNS|NNP|NN|NNPS>{1,2}}      # E.g. 6 astronomical units, 1 alpha TE, 1 square meter, 3 cubic inch, 1 atomic mass unit, 1 British shipping ton
                {<CD> <JJ> <JJ> <NNS>? <IN>? <NN|NNP>}  # E.g. 1 actual cubic centimeters per minute, 1 modified Julian NN
                {<CD> <VBG> <JJ> <NN>}                  # E.g. 1 cooling degree day
                {<CD> <CD|IN|$>}                        # E.g. 328 billion, 1 as, 1 at, 1 $
        """
        cp = nltk.RegexpParser(unit_chunker_grammar)

        # read from unit_gazetteer
        gazetteer = defaultdict(set)
        with open("unit_gazetteer.txt", "r") as f:
            for line in f:
                pos, word = line.split()
                gazetteer[pos].add(word)

        for i in range(len(self.pos_tags)):
            tree = cp.parse(self.pos_tags[i])
            for subtree in tree.subtrees():
                if subtree.label() == 'UN':
                    tup_list = subtree.leaves()
                    tup_units = tup_list[1:]    # ignore the first <CD>

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
