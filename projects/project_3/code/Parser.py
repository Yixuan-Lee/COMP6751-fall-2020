import os
from nltk import load_parser, FeatureEarleyChartParser
from typing import List, Tuple, Dict
from nltk.draw.tree import TreeView
from collections import defaultdict


class SentParser:
    def __init__(self, grammar_url_s: str, print: bool = False, draw: bool = False, save: bool = False):
        """
        constructor
        :param grammar_url_s: grammar file URL
        :param print: whether print the tree on console
        :param draw: whether draw the parse tree on console
        :param save: whether save the parse tree on drive
        """
        self.cp_s = load_parser(grammar_url_s, trace=0, parser=FeatureEarleyChartParser)
        self.print = print
        self.draw = draw
        self.save = save
        self.tree_no = 1

    def parse(self, tokens: List[str]) -> Tuple[list, Dict[str, List[str]]]:
        """
        parse sentences in sent and print the parse tree
        :param tokens: tokens of a sentence
        :return all possible sentiment labels
        """
        sentiment = []
        parse_trees: Dict[str, List[str]] = defaultdict(list)

        # parse the sentence where S is the root
        for tree in self.cp_s.parse(tokens):
            if self.print:
                print(tree)
            if self.draw:
                tree.draw()
            if self.save:
                # save the tree diagram
                TreeView(tree)._cframe.print_to_file('saved_results/Tree' + str(self.tree_no) + '_diagram.ps')
                # save the tree text
                with open('saved_results/Tree' + str(self.tree_no) + '_text.txt', "w", encoding='utf-8') as writer:
                    writer.write(str(tree))
            # append the root's SENTI attribute value to the list
            senti_label = tree.label()['SENTI']
            if senti_label in ['negative', 'positive', 'neutral']:
                sentiment.append(senti_label)
                parse_trees[senti_label].append(str(tree))
            self.tree_no += 1
        if len(sentiment) == 0:
            sentiment.append('unknown')
            parse_trees['unknown'].append('(unknown)')

        return sentiment, parse_trees

    def clear_directory(self) -> None:
        """
        clear the saved_results directory
        """
        if self.save:
            # delete all files in ./saved_results/ directory
            dir = 'saved_results/'
            filelist = [f for f in os.listdir(dir)]
            for f in filelist:
                os.remove(os.path.join(dir, f))
