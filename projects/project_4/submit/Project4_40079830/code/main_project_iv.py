from Pipeline import SentimentPipeline
from Parser import SentParser
from Lexica import DataLoader


if __name__ == '__main__':
    # define the parser
    grammar_url_s = 'grammar/sentianalysis_grammar_s.fcfg'
    parser = SentParser(grammar_url_s, False, False, False)
    # load the data from nltk
    data = DataLoader()

    # define and run pipeline
    sp = SentimentPipeline(parser, data)
    # sp.print_lexica()
    sp.run_pipeline()
    print()
    print("The results are saved in the file 'saved_results/Good.txt' and 'saved_results/False.txt'.")

    print()
    print("Baseline SSAP performance:")
    sp.baseline.performance()
    print()
    print("Project IV performance:")
    sp.performance()
