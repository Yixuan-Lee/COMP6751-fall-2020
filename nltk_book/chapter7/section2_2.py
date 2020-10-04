import nltk

sentence = [("another", "DT"), ("sharp", "JJ"), ("dive", "NN"), ("trade", "NN"), ("figures", "NNS"), ("any", "DT"),  ("new", "JJ"), ("policy", "NN"), ("measures", "NNS"), ("earlier", "JJR"), ("stages", "NNS"), ("Panamanian", "JJ"), ("dictator", "NN"), ("Manuel", "NNP"), ("Noriega", "NNP")]
grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)
result.draw()