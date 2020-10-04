import nltk
from nltk.tokenize import RegexpTokenizer

# TODO: comment this out if reuters corpus has downloaded on local
nltk.download('reuters')    # download reuters corpora

from nltk.corpus import reuters # import reuters corpora
from typing import List
from MeasuredEntityDetection import UnitEntityDetector
from DateRecognizer import DateRecognizer
from DateParser import DateParser


class Pipeline:
    def __init__(self, fileid: str):
        self.fileid = fileid
        self.raw_text = ""
        self.save_file_name = 'reuters-' + self.fileid.replace('/', '-') + '.txt'

    def read_raw_and_save(self):
        """
        read fileid file from reuters corpus from NLTK and write it on local
        :return: True if successful, otherwise False
        """
        if self.fileid in reuters.fileids():
            # get the text using the NLTK corpus
            self.raw_text = reuters.raw(self.fileid)
        else:
            raise Exception('Error: ' + str(fileid) + ' does not exist in reuters corpus.')

        # save the raw text on local for backup
        with open(self.save_file_name, "w") as f:
            f.write(self.raw_text)

    def split_title_and_body(self):
        # replace the html symbols with actual symbols
        self.raw_text = self.raw_text.replace('&lt;', '<')
        self.raw_text = self.raw_text.replace('&gt;', '>')

        # split title and body content
        title, body = self.raw_text.split('\n', 1)

        # check if split is successful
        # check if title is in uppercase
        if title.upper() != title:
            print('Warning: this file does not have a title.')
            # consider all contents as body
            body = title + body
            return "", body
        else:
            return title, body

    def reformat_body(self, body: str) -> str:
        """
        Due to the body text may have new lines in the middle of a sentence,
        perform a reformation before processing
        :param body: body content
        :return: one-line reformed body
        """
        reformed_body = ""
        for line in body.split('\n'):
            reformed_body += line.strip() + ' '
        return reformed_body

    def pre_process(self, tokenizer_type: str, tokenizer_types: List[str]):
        try:
            # read the text from NLTK
            self.read_raw_and_save()

            # get the title and body contents
            title, body = self.split_title_and_body()

            # reformat the body as the text in assignment description
            body = self.reformat_body(body)

            ############################ Pipeline ############################
            # 1. tokenization
            if tokenizer_type == tokenizer_types[0]:
                # use basic regular expression tokenzier (not enhanced) from NLTK book chapter 3
                pattern = r'''(?x)              # set flag to allow verbose regexps
                        (?:[A-Z]\.)+            # abbreviations, e.g. U.S.A.
                      | \w+(?:-\w+)*            # words with optional internal hyphens
                      | \$?\d+(?:\.\d+)?%?      # currency and percentages, e.g. $12.40, 82%
                      | \.\.\.                  # ellipsis
                      | [][.,;"'?():-_`]        # these are separate tokens; includes ], [
                      '''
            elif tokenizer_type == tokenizer_types[1]:
                # use enhanced regular expression tokenizer based on basic regular expression tokenizer
                pattern = r'''(?x)                  # set flag to allow verbose regexps
                        (?:[A-Z]\.)+                # abbreviations, e.g. U.S.
                      | \$?\d+(?:,\d+)?(?:\.\d+)?%? # currency or percentages or numbers that include a comma and/or a period e.g. $12.50, 52.25%, 30,000, 3.1415, 1,655.8
                      | \w+(?:-\w+)*                # words with optional internal hyphens e.g. state-of-the-art
                      | \.\.\.                      # ellipsis ...
                      | \'[sS]                      # tokenize "'s" together
                      | [][.,;"'?():-_`]            # these are separate tokens; include ], [
                      | \w+                         # word characters
                      '''
            else:
                raise Exception("Error: tokenizer type \'" + str(tokenizer_type) + "\' does not exist in [" + (', '.join(tokenizer_types)) + '].')

            regex_tokenizer = RegexpTokenizer(pattern)
            title_tokens = regex_tokenizer.tokenize(title)
            body_tokens = regex_tokenizer.tokenize(body)
            print('Tokenization results:')
            print(title_tokens)
            print(body_tokens)
            print('---------------------------------------------')

            # 2. sentence splitting
            # ## use built-in tagged sentence (for clarify)
            body_sents = nltk.sent_tokenize(body)
            print('Sentences splitting results:')
            print(body_sents)
            print('---------------------------------------------')

            # 3. POS tagging
            pos_tags: List[List[str]] = list()
            for body_sent in body_sents:
                body_tokens = regex_tokenizer.tokenize(body_sent)
                body_pos_tags = nltk.pos_tag(body_tokens)
                pos_tags.append(body_pos_tags)
            print('Part-of-speech tagging results:')
            print(pos_tags)
            print('---------------------------------------------')

            # 4. number normalization
            # has implemented in `pattern` during tokenization step

            # measured entity detection
            ud = UnitEntityDetector(pos_tags)
            unit_entity = ud.unit_detection()   # get a list of unit entities
            print('Measured entity detection:')
            print(unit_entity)
            print('---------------------------------------------')

            # 5. date recognition
            dr = DateRecognizer(pos_tags)
            dates = dr.recognize_dates()    # get a list of detected dates
            print('Date recognition:')
            print(dates)
            print('---------------------------------------------')

            # 6. date parsing
            dp = DateParser(body_sents, pos_tags)
            print('Date parsing:')
            dp.date_parse(dates) # parse the dates detected by date recognizer

        except Exception as ex:
            print(ex.args[0])


if __name__ == '__main__':
    # TODO: change the fileid for different test cases
    # test cases used in report and demo
    #      training/267
    #      training/279
    #      training/6
    fileid = 'training/267'
    PreProcess = Pipeline(fileid)   # initialization

    tokenizer_types = ['base', 'enhanced']
    PreProcess.pre_process(tokenizer_types[1], tokenizer_types)
