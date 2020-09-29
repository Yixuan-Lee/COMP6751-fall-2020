import nltk
import re   # regular expression
from nltk.tokenize import RegexpTokenizer

# download and import reuters corpus
# TODO: uncomment this line before submission
# nltk.download('reuters')
from nltk.corpus import reuters
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
        # title should be all uppercase
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
            print('1. ---------------------------------------------')
            print('title:', title)
            print('body:', body)

            # reformat the body as the text in assignment description
            body = self.reformat_body(body)
            print('2. ---------------------------------------------')
            print('body:', body)

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
                # use enhanced regular expression tokenizer based on basic regular expression
                pattern = r'''(?x)                  # set flag to allow verbose regexps
                        (?:[A-Z]\.)+                # abbreviations, e.g. U.S.
                      | \$?\d+(?:,\d+)?(?:\.\d+)?%? # currency or percentages or numbers that include a comma and/or a period e.g. $12.50, 52.25%, 30,000, 3.1415, 1,655.8
                      | \w+(?:-\w+)*                # words with optional internal hyphens e.g. state-of-the-art
                      | \.\.\.                      # ellipsis ...
                      | \'s                         # tokenize "'s" together
                      | [][.,;"'?():-_`]            # these are separate tokens; include ], [
                      | \w+                         # word characters
                      '''
            else:
                raise Exception("Error: tokenizer type \'" + str(tokenizer_type) + "\' does not exist in [" + (', '.join(tokenizer_types)) + '].')

            regex_tokenizer = RegexpTokenizer(pattern)
            title_tokens = regex_tokenizer.tokenize(title)
            body_tokens = regex_tokenizer.tokenize(body)
            print('3. ---------------------------------------------')
            print(title_tokens)
            print(body_tokens)
            print(len(title_tokens))
            print(len(body_tokens))

            # 2. sentence splitting
            # ## use built-in tagged sentence (for clarify)
            body_sents = nltk.sent_tokenize(body)
            print('4. ---------------------------------------------')
            print(body_sents)
            print(len(body_sents))
            '''
            # ## split sentences based on the results of tokenization (this can replace nltk.sent_tokenize(body) above.)
            title_sent = [t for t in title_tokens]
            index_2_split = [index + 1 for index, value in enumerate(body_tokens) if value == '.']
            body_sents = [body_tokens[i:j] for i, j in zip([0] + index_2_split, index_2_split + ([len(body_tokens)] if index_2_split[-1] != len(body_tokens)  else []))]
            print('5. ---------------------------------------------')
            print(title_sent)
            print(body_sents)
            '''
            # 3. POS tagging
            pos_tags: List[List[str]] = list()
            for body_sent in body_sents:
                body_tokens = regex_tokenizer.tokenize(body_sent)
                body_pos_tags = nltk.pos_tag(body_tokens)
                pos_tags.append(body_pos_tags)
            print('6. ---------------------------------------------')
            print(pos_tags)

            # 4. number normalization
            # has implemented in `pattern` during tokenization process

            # measured entity detection
            ud = UnitEntityDetector(pos_tags)
            unit_entity = ud.unit_detection()
            print('7. ---------------------------------------------')
            print(unit_entity)

            # 5. date recognition
            dr = DateRecognizer(pos_tags)
            dates = dr.recognize_dates()
            print('8. ---------------------------------------------')
            print(dates)

            # 6. date parsing
            dp = DateParser(body_sents, pos_tags)
            dp.date_parse(dates)

        except Exception as ex:
            print(ex.args[0])



if __name__ == '__main__':
    fileid = 'training/555'
    # initialization
    PreProcess = Pipeline(fileid)

    tokenizer_types = ['base', 'enhanced']
    PreProcess.pre_process(tokenizer_types[1], tokenizer_types)

