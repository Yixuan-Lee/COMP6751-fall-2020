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

3. [Pattern delimiter (?:pattern) in regular expressions](http://www.javascriptkit.com/javatutors/redev2.shtml)

4. [RegexpTokenizer](https://www.nltk.org/_modules/nltk/tokenize/regexp.html)

5. [NLTK实现文本切分](https://www.cnblogs.com/zrmw/p/10875684.html)

6. [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)

7. [Using integers/dates as terminals in NLTK parser](https://stackoverflow.com/questions/4148171/using-integers-dates-as-terminals-in-nltk-parser)

8. [python - 如何在NLTK CFG中匹配整数？](https://www.coder.work/article/3169703)

9. [List of Units / Measurements](https://www.hobbyprojects.com/dictionary_of_units.html)

10. [re Regular expression operations documentation](https://docs.python.org/3/library/re.html#regular-expression-syntax)

11. [re Regular expression operations documentation 2](https://docs.python.org/2/library/re.html)

12. [In Python, how do I split a string and keep the separators?](https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators?lq=1)

13. [Units of Measurement Word Wall Vocabulary](https://www.teachstarter.com/au/teaching-resource/units-of-measurement-word-wall-vocabulary/)


