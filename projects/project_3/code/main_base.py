from Pipeline import SentimentPipeline
from Parser import SentParser
from Lexica import DataLoader


if __name__ == '__main__':
    # define the parser
    grammar_url = 'grammar/sentianalysis_grammar.fcfg'
    parser = SentParser(grammar_url, False, False, False)
    # load the data from nltk
    data = DataLoader()

    # define and run pipeline
    sp = SentimentPipeline(parser, data)
    sp.print_lexica()
    # sp.run_pipeline()

