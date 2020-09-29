import re
import nltk
from typing import List, Set


class DateRecognizer:

    def __init__(self, pos_taggings: List[List[str]]):
        self.pos_tags = pos_taggings
        self.date_list: Set[str] = set()
        self.month = ('January','February','March','April','May','June',
            'July','August','September','October','November','December',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
        self.date_patterns = "(\d{4}[-/]?\d{2}[-/]?\d{2})"\
               "|(\w+\s\d{1,2}[a-zA-Z]{2},?\s?\d{4}?)"\
               "|(the\s\d{1,2}[a-zA-Z]{2}\sof\s[a-zA-Z]+)"\
               "|(the\s\w+\sof\s\w+)"\
               "|(\w+\s\d{1,2}[a-zA-Z]{2})"\
               "|(\w+\s\d{1,2})"
        self.date_regex = re.compile(self.date_patterns)

    def recognize_dates(self) -> Set[str]:
        # extract different format of dates from the each sentence
        DateRecognizerCFG = r"""
            DATE:   {<IN> <NNP> <CD> <,>? <CD>}     # E.g. December 12th, 2020
                    {<IN> <DT> <NN> <IN> <NNP>}     # E.g. the twelfth of December
                    {<IN> <DT> <CD> <IN> <NNP>}     # E.g. the 12th of December
                    {<IN> <NNP> <CD>}               # E.g. in December 12th
                    {<NNP> <CD>}                    # E.g. March 30
                    {<IN> <CD>}                     # E.g. in 2020, in 2020/12/12
        """
        cp = nltk.RegexpParser(DateRecognizerCFG)

        for i in range(len(self.pos_tags)):
            tree = cp.parse(self.pos_tags[i])
            # tree.draw()
            for subtree in tree.subtrees():
                if subtree.label() == 'DATE':
                    tokens = [tup[0] for tup in subtree.leaves()]
                    if '/' in tokens:
                        date = ''.join(ch for ch in tokens)
                    else:
                        date = ' '.join(word for word in tokens)

                    # check if date satisfies all conditions
                    validity = self.date_validity_check(date, tokens)

                    if validity:
                        self.date_list.add(date)

        return self.date_list

    def date_validity_check(self, date_str: str, tokens: List[str]) -> bool:
        # traverse tokens to check if numbers are valid
        for token in tokens:
            if token != ('/' or '-') and not token.isalnum():
                # meaning that tokens may have float, special characters or non-alphanumeric characters
                return False

        # check if data_str satisfies the date_patterns
        check = self.date_regex.findall(date_str)
        if len(check) == 0 or check == []:
            return False

        return True
