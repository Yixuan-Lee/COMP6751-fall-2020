import os
import nltk
from nltk import sent_tokenize, word_tokenize, load_parser, FeatureEarleyChartParser
from nltk.tag.stanford import StanfordNERTagger, StanfordPOSTagger
from typing import List, Tuple


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
        for tree in self.cp.parse(tokens):
            print(tree)     # print the tree
            # tree.draw()     # display the tree diagram


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
        If text in raw data file contains multiple lines, then merge into 1 lines split by a space.
        :return one-line reformed body
        """
        reformed_raw = ""
        for line in self.raw.split('\n'):
            reformed_raw += line.strip() + ' '
        return reformed_raw

    def part_of_speech_tagging(self, words: List[str]) -> List[Tuple[str, str]]:
        """
        perform part-of-speech tagging using StanfordPOSTagger
        :param sent: a sentence
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
        return normal_pos_tag

    def name_entity_module(self, word_list: List[str]) -> List[str]:
        """
        perform named entity recognition using StanfordPOSTagger
        :param pos_tags: pos taggings
        :return: part-of-speech tags after merging name entities in sentences
        """
        path_to_model = 'stanford/ner/english.all.3class.distsim.crf.ser.gz'
        path_to_jar = 'stanford/ner/stanford-ner.jar'
        ner = StanfordNERTagger(path_to_model, path_to_jar)
        entity_list = ner.tag(word_list)
        # merge words which belong to the same name entity
        def merge(entity_list: List[Tuple[str, str]]) -> None:
            for (index, (word, tag)) in enumerate(entity_list):
                if tag == 'O':
                    continue
                else:
                    # hitting a multi-word name entity, start merging
                    name_entity = [word]
                    entity_tag = tag
                    i = index + 1
                    while i < len(entity_list):
                        next_word, next_tag = entity_list[i]
                        if next_tag == entity_tag:  # check if they belongs to the same tag
                            name_entity.append(next_word)
                            _ = entity_list.pop(i)
                        else:
                            break
                    entity_list[index] = (' '.join(name_entity), entity_tag)
        merge(entity_list)
        return [entity for (entity, tag) in entity_list]

    def parse_and_validate(self, tokens: List[List[str]], pos_tags: List[List[str]]) -> None:
        """
        parse the sentences and print the parse trees
        :param pos_tags: pos taggings
        """
        for ts in tokens:
            self.parser.parse(ts)

    def run_validation(self):
        try:
            # read the text from a local file
            self.read_raw_data()
            # reformat the text
            raw = self.reformat_raw()

            # sentence splitting
            sents = nltk.sent_tokenize(raw)
            print('Sentences splitting results:')
            print(sents)
            print('---------------------------------------------')

            # tokenization + pos tagging
            pos_tags: List[List[str]] = list()
            tokens: List[List[str]] = list()
            for sent in sents:
                # word tokenization
                words = word_tokenize(sent)
                # name entity module
                words = self.name_entity_module(words)
                tokens.append(words[:-1])   # omit the last period
                # part-of-speech tagging
                pos_tags.append(self.part_of_speech_tagging(words))
            print('Part-of-speech tagging results:')
            print(pos_tags)
            print('---------------------------------------------')

            # run the Earley parser written in context-free grammar to validate data
            print('Parsing results:')
            self.parse_and_validate(tokens, pos_tags)
            print('---------------------------------------------')

        except Exception as ex:
            print(ex.args[0])


if __name__ == '__main__':
    # define an Earley parser and load the grammar rules
    grammar_file_url = 'grammar/grammar.fcfg'
    parser = Parser(grammar_file_url)

    # TODO: this is the testing file path, please change the path to the testing file before testing
    data_file = 'data/sent1.txt'

    # run pipeline to validate the data
    pipeline = Pipeline(parser, data_file)
    pipeline.run_validation()

