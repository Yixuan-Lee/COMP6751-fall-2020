"""
This is the enhanced version which use StanfordPOSTagger and StanfordNERTagger
for POS Tagging and Name Entity Module. I will compare the result with the
base version (main_base) in my report.
"""

import os
import nltk
from nltk import sent_tokenize, word_tokenize, load_parser, FeatureEarleyChartParser
from nltk.tag.stanford import StanfordNERTagger, StanfordPOSTagger
from nltk.draw.tree import TreeView
from typing import List, Tuple, Set


class Parser:
    def __init__(self, grammar_url: str, pprint: bool=False, save: bool=False):
        """
        constructor
        :param grammar_url: grammar file URL
        """
        self.cp = load_parser(grammar_url, trace=0, parser=FeatureEarleyChartParser)
        self.print = pprint
        self.save = save
        self.tree_no = 1

    def parse(self, tokens: List[str]) -> None:
        """
        parse sentences in sent and print the parse tree
        :param sentences: sentences
        """
        for tree in self.cp.parse(tokens):
            print(tree)     # print the tree
            if self.print:
                tree.draw()     # display the tree diagram
            if self.save:
                TreeView(tree)._cframe.print_to_file('results/output' + str(self.tree_no) + '.ps')
            self.tree_no += 1


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
        # define pos tagger
        path_to_model = 'stanford/pos/english-bidirectional-distsim.tagger'
        path_to_jar = 'stanford/pos/stanford-postagger.jar'
        pos_tagger = StanfordPOSTagger(path_to_model, path_to_jar)

        stan_pos_tag = pos_tagger.tag(words[:-1])   # omit the last period
        normal_pos_tag = nltk.pos_tag(words[:-1])   # omit the last period
        # print('Stanford POS tagging:', stan_pos_tag)        # for comparison
        # print('nltk.pos_tag tagging:', normal_pos_tag)      # for comparison

        def post_treatment(stan_pos_tag: List[Tuple[str, str]], norm_pos_tag: List[Tuple[str, str]], multi_word_name_entities: Set[str]) -> None:
            """
            combine the multi-word name entities
            since nltk.pos_tag label multi-word name entities together, so I correct stan_pos_tag by using norm_pos_tag
            the problem of norm_pos_tag is that it usually mislabels words, and that's why I prefer to use StanfordPOStagger
            :param stan_pos_tag: a list of pos-tags of sentences using stanford pos tagger
            :param norm_pos_tag: a list of pos-tags of sentences using nltk.pos_tag
            """
            stan_len = len(stan_pos_tag)
            norm_len = len(normal_pos_tag)
            stan_i = 0
            norm_i = 0
            while stan_i < stan_len and norm_i < norm_len:
                stan_word, stan_pos = stan_pos_tag[stan_i]
                norm_word, norm_pos = norm_pos_tag[norm_i]
                # check if word exists in multi_word_name_entities
                if stan_word == norm_word.split(' ')[0] and norm_word in multi_word_name_entities:
                    # scan the following words in stan_pos_tag and combine if they can form a multi-word entity
                    temp_i = stan_i + 1
                    match_idx = 1
                    entities = norm_word.split(' ')
                    while temp_i < stan_len and match_idx < len(entities):
                        temp_word, temp_pos = stan_pos_tag[temp_i]
                        if temp_word == entities[match_idx]:
                            _ = stan_pos_tag.pop(temp_i)
                            match_idx += 1
                        else:
                            break
                    stan_pos_tag[stan_i] = (norm_word, stan_pos)
                stan_i += 1
                norm_i += 1

        post_treatment(stan_pos_tag, normal_pos_tag, multi_word_name_entities)

        return stan_pos_tag

    def name_entity_module(self, word_list: List[str]) -> Tuple[List[str], Set[str]]:
        """
        perform named entity recognition using StanfordNERTagger
        :param word_list: token list
        :return: a token list after merging name entities + a set of name entities
        """
        path_to_model = 'stanford/ner/english.all.3class.distsim.crf.ser.gz'
        path_to_jar = 'stanford/ner/stanford-ner.jar'
        ner = StanfordNERTagger(path_to_model, path_to_jar)
        entity_list = ner.tag(word_list)
        # this multi_word_name_entities is to solve the problem in StanfordPOSTagger.
        # If I intend to use StanfordPOSTagger, it always pos-tag multi-word entites separately,
        # such as "John O'Malley" in sample 8 even though I have combined "John" and "O'Malley"
        # together as "John O'Malley" in this name_entity_module
        # So I record all name entities and do a post-treatment after I get the result from StanfordPOSTagger
        # in function part_of_speech_tagging to make sure that name entities are combined.
        name_entities: Set[str] = set()
        # merge words which belong to the same name entity
        def merge(entity_list: List[Tuple[str, str]]) -> None:
            for (index, (word, tag)) in enumerate(entity_list):
                if tag == 'O':  # other tags
                    continue
                else:           # PERSON or LOCATION or ORGANIZATION
                    # hitting a multi-word name entity, start merging
                    name_entity = [word]
                    entity_tag = tag
                    i = index + 1
                    while i < len(entity_list):
                        next_word, next_tag = entity_list[i]
                        if next_tag != entity_tag:
                            break
                        else:  # if they belongs to the same tag
                            name_entity.append(next_word)
                            _ = entity_list.pop(i)
                    entity_list[index] = (' '.join(name_entity), entity_tag)
                    if len(name_entity) >= 1:
                        name_entities.add(' '.join(name_entity))
        merge(entity_list)
        return [entity for (entity, tag) in entity_list], name_entities

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

        except Exception as ex:
            print(ex.args[0])


if __name__ == '__main__':
    # define an Earley parser and load the grammar rules
    input_pprint = input('Do you want to print the parse trees on the console? (Y/N) ')
    input_save = input('Do you want to save the parse tree diagrams in the directory ./result/? (Y/N) ')
    pprint = False
    save = False
    if input_pprint == 'Y' or input_pprint.lower() == 'Yes':
        pprint = True
    if input_save == 'Y' or input_save.lower() == 'Yes':
        save = True
    grammar_file_url = 'grammar/grammar.fcfg'
    parser = Parser(grammar_file_url, pprint, save)

    # TODO: this is the file path to read and parse, please change the path to the testing file path
    data_file = 'data/sent9.txt'

    # run pipeline to validate the data
    pipeline = Pipeline(parser, data_file)
    pipeline.run_validation()

