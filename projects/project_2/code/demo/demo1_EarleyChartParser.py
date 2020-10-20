import nltk
from nltk.parse.chart import demo_grammar


if __name__ == '__main__':
    grammar = nltk.CFG.fromstring("""
        S -> NP VP
        VP -> V NP | V
        NP -> NAME | ART N
        NAME -> 'John'
        V -> 'ate'
        ART -> 'the'
        N -> 'cat'
        """)

    tokens = ['John', 'ate', 'the', 'cat']

    print(demo_grammar())

    parser = nltk.parse.earleychart.EarleyChartParser(grammar, trace=1)
    for tree in parser.parse(tokens):
        print(tree)
