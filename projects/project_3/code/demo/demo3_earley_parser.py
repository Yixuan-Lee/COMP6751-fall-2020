import nltk
from nltk import load_parser, FeatureEarleyChartParser


if __name__ == '__main__':
    tokens = nltk.word_tokenize("He is horrible")
    print(tokens)
    parser = load_parser(grammar_url='../grammar/demo_senti_grammar.fcfg', trace=0, parser=FeatureEarleyChartParser)
    for tree in parser.parse(tokens):
        print(tree)
        print(type(tree.label()))
        print(tree.label())
        # retrieve the senti label of the root node
        print(tree.label()['senti'])
