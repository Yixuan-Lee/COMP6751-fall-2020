# Project 1 README

# 1. Tokenization

Enhancement:

Compare my `pattern` in tokenization period and the regular expression under *Table 3.4*
on the [website](http://www.nltk.org/book/ch03.html#tab-re-symbols).

```text
>>> text = 'That U.S.A. poster-print costs $12.40...'
>>> pattern = r'''(?x)     # set flag to allow verbose regexps
...     (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
...   | \w+(?:-\w+)*       # words with optional internal hyphens
...   | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
...   | \.\.\.             # ellipsis
...   | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
... '''
```



# 2. Sentence Splitting

# 3. POS (Part-Of-Speech) tagging

# 4. Number Normalization

# Open-ended task: Measured Entity Detection

# 5. Date Recognition

# 6. Date Parsing


# References

1. [Python regular expression (regex) match comma separated number - why does this not work?](https://stackoverflow.com/questions/16321007/python-regular-expression-regex-match-comma-separated-number-why-does-this-n)

2. [Python | Split list into lists by particular value](https://www.geeksforgeeks.org/python-split-list-into-lists-by-particular-value/)
