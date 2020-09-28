import nltk
import re   # regular expression
from nltk.tokenize import RegexpTokenizer


# download and import reuters corpus
# nltk.download('reuters')
from nltk.corpus import reuters

# Get the text using the NLTK corpus
fileid = 'training/267'
raw_text = reuters.raw(fileid)
print('1. ---------------------------------------------')
print(raw_text)

# Save the text into a local file
filename = 'reuters-training-267.txt'
out_file = open(filename, "w")
out_file.write(raw_text)
out_file.close()


def PreProcess(file):
    """
    :param file: the reuter training file
    """
    # read the text in file
    with open(file) as f:
        raw = f.read()
    print('2. ---------------------------------------------')
    print(raw)

    title, body = raw.split('\n', 1)
    print('3. ---------------------------------------------')
    print('title:', title)
    print('body:', body)

    # reformat the body as the text in assignment description
    print('4. ---------------------------------------------')
    reformat_body = ""
    for line in body.split('\n'):
        reformat_body += line.strip() + ' '
    print(reformat_body)

    ############################ Pipeline ############################
    # 1. tokenization
    # with a regular expression based tokenizer from NLTK
    pattern = r'''(?x)          # set flag to allow verbose regexps
        (?:[A-Z]\.)+            # abbreviations, e.g. U.S.A., U.S.
        | \$?\d+(?:,\d+)?(?:\.\d+)?%?   # currency or percentages or numbers that include a comma or a period e.g. $12.50, 52.25%, 30,000, 3.1415, 1,655.8
        | \w+(?:-\w+)*          # words with optional internal hyphens e.g. state-of-the-art
        | \.\.\.                # ellipsis ...
        | [][.,;"'?():-_`]      # these are separate tokens; include ], [
        | \w+                   # word characters
    '''
    regex_tokenizer = RegexpTokenizer(pattern)
    title_tokens = regex_tokenizer.tokenize(title)
    body_tokens = regex_tokenizer.tokenize(reformat_body)
    print('5. ---------------------------------------------')
    print(title_tokens)
    print(body_tokens)
    print(len(title_tokens))
    print(len(body_tokens))

    # 2. sentence splitting
    # ## use built-in tagged sentence (for clarify)
    sens = reuters.sents('training/267')
    print('6. ---------------------------------------------')
    print(sens)
    print(len(sens))

    # ## split sentences based on the results of tokenization
    title_sent = [t for t in title_tokens]
    index_2_split = [index + 1 for index, value in enumerate(body_tokens) if value == '.']
    body_sents = [body_tokens[i:j] for i, j in zip([0] + index_2_split, index_2_split + ([len(body_tokens)] if index_2_split[-1] != len(body_tokens)  else []))]
    print('7. ---------------------------------------------')
    print(title_sent)
    print(body_sents)

    # 3. POS tagging
    pos_tagging = []
    print('8. ---------------------------------------------')
    print(nltk.pos_tag(body_tokens))

    # 4. number normalization




PreProcess(filename)
