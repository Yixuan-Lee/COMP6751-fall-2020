"""
Chapter 3 section 3.1 Accessing Text from the Web and from Disk

website: http://www.nltk.org/book/ch03.html

"""

from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request

print('--------------------- a. ------------------------')
# ## a. specify the proxy manually before downloading
# proxies = {'http': 'http://www.someproxy.com:3128'}
# request.ProxyHandler(proxies)
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(type(raw))
print(len(raw))
print(raw[:75])

# ## tokenization: break up the string into words and punctuation
print('--------------------- b. ------------------------')
tokens = word_tokenize(raw)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

# ## regular list operations like slicing
print('--------------------- c. ------------------------')
text = nltk.Text(tokens)
print(type(text))
print(text[1024:1062])
print(text.collocations)

# ## find() and rfind(): get the right index
print('--------------------- d. ------------------------')
print(raw.find("PART I"))
print(raw.rfind("End of Project Gutenberg's Crime"))
raw = raw[5338:1157743]
print(raw.find("PART I"))

# ## Dealing with HTML
print('--------------------- e. ------------------------')
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
print(html[:60])

from bs4 import BeautifulSoup
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)
print(tokens)

# ## With some trial and error you can find the start and end indexes of the content
tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')

# ## Processing search engine results
print('--------------------- e. ------------------------')