"""
This is the base version which use nltk.pos_tag and nltk.ne_chunk for POS Tagging
and Name Entity Module.
"""


import os
import nltk
from nltk import sent_tokenize, word_tokenize, load_parser, FeatureEarleyChartParser
from typing import List, Tuple, Set

# TODO: uncomment the two lines before submission
# nltk.download('maxent_ne_chunker')
# nltk.download('words')


class Parser:
    def __init__(self, grammar_url: str):
        """
        constructor
        :param grammar_url: grammar file URL
        """
        self.cp = load_parser(grammar_url, trace=0, parser=FeatureEarleyChartParser)

    def parse(self, tokens: List[str]) -> None:
        """
        parse sentences in sent and print the parse tree
        :param sentences: sentences
        """
        trees = 0
        for tree in self.cp.parse(tokens):
            print(tree)     # print the tree
            # tree.draw()     # display the tree diagram
            trees += 1
        print('trees =', trees)


class Pipeline:
    def __init__(self, parser: Parser, sent_url: str):
        """
        constructor
        :param parser: parser that will be used in pipeline
        """
        self.parser = parser
        self.sent_url = sent_url
        self.raw = None

    def read_raw_data(self):
        """
        read raw data from the url
        """
        # check data file validity and read sentence from the file
        sent_url = self.sent_url
        if os.path.exists(sent_url):
            with open(sent_url) as file:
                self.raw = file.read()
        else:
            raise Exception('Error: ' + sent_url + ' does not exist on local.')

    def reformat_raw(self) -> str:
        """
        If text in raw data file contains multiple lines, then merge into 1 lines separated by a space.
        :return one-line reformed raw text
        """
        reformed_raw = ""
        for line in self.raw.split('\n'):
            reformed_raw += line.strip() + ' '
        return reformed_raw

    def part_of_speech_tagging(self, words: List[str], multi_word_name_entities: Set[str]) -> List[Tuple[str, str]]:
        """
        perform part-of-speech tagging using StanfordPOSTagger
        :param words: a list of words in a sentence
        :param multi_word_name_entities: a set of multi-word name entities
        :return: part-of-speech tag of the sentence
        """
        normal_pos_tag = nltk.pos_tag(words[:-1])   # omit the last period

        return normal_pos_tag

    def name_entity_module(self, word_list: List[str]) -> Tuple[List[str], Set[str]]:
        """
        perform named entity recognition using StanfordNERTagger
        :param word_list: token list
        :return: a token list after merging name entities + a set of name entities
        """
        pos_tag_list = nltk.tag.pos_tag(word_list)  # do POS tagging before chunking
        ne_parse_tree = nltk.ne_chunk(pos_tag_list)
        name_entities: Set[str] = set()
        word_list_merged: List[str] = list()

        for node in ne_parse_tree:
            if isinstance(node, nltk.tree.Tree) and node.label() in ['PERSON', 'ORGANIZATION', 'GPE']:
                ne = ' '.join([word for (word, tag) in node.leaves()])
                name_entities.add(ne)
                word_list_merged.append(ne)
            elif isinstance(node, tuple):
                word_list_merged.append(node[0])
            elif isinstance(node, str):
                word_list_merged.append(node)
        return word_list_merged, name_entities

    def parse_and_validate(self, token_lists: List[List[str]], pos_tags: List[List[str]]) -> None:
        """
        parse the sentences and print the parse trees
        :param token_lists: a list of token lists of sentences
        """
        for ts in token_lists:
            self.parser.parse(ts)

    def run_validation(self):
        try:
            # read the text from a local file
            self.read_raw_data()
            # reformat the text
            raw = self.reformat_raw()

            # sentence splitting
            sents = sent_tokenize(raw)
            print('Sentences splitting results:')
            print(sents)
            print('---------------------------------------------')

            # tokenization + pos tagging
            pos_tags: List[List[str]] = list()
            token_lists: List[List[str]] = list()
            name_entities: Set[str] = set()
            for sent in sents:
                # word tokenization
                words = word_tokenize(sent)
                # name entity module
                words, name_entity = self.name_entity_module(words)
                token_lists.append(words[:-1])   # omit the last period
                name_entities = name_entities.union(name_entity)
                # part-of-speech tagging
                pos_tags.append(self.part_of_speech_tagging(words, name_entity))
            print('Part-of-speech tagging results:')
            print(pos_tags)
            print('Name entities:')
            print(name_entities)
            print('---------------------------------------------')

            # run the Earley parser written in context-free grammar to validate data
            print('Parsing results:')
            self.parse_and_validate(token_lists, pos_tags)
            print('---------------------------------------------')

        except Exception as ex:
            print(ex.args[0])


if __name__ == '__main__':
    # define an Earley parser and load the grammar rules
    grammar_file_url = 'grammar/grammar_base.fcfg'
    parser = Parser(grammar_file_url)

    # TODO: this is the file path to read and parse, please change the path to the testing file path
    # data_file = 'data/sent7.txt'
    data_file = 'data/sent9.txt'

    # run pipeline to validate the data
    pipeline = Pipeline(parser, data_file)
    pipeline.run_validation()

