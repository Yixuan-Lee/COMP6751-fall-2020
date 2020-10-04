"""
Use beautifulsoup to parse Unit of Measurement websites to extract units

References:
https://www.dataquest.io/blog/web-scraping-beautifulsoup/

"""

import re
from requests import get
from bs4 import BeautifulSoup

url = 'http://www.ibiblio.org/units/dictA.html'
response = get(url)
print(response.text)
print('-----------------------------------------------------------------')

# use beautifulsoup to parse the HTML content
# html_soup = BeautifulSoup(response.text, 'html.parser')
# # print(type(html_soup))
# print(html_soup.find('DT'))

str = response.text
match1 = re.findall(r'<DT><B>.*</B></DT>', str)
match2 = re.findall(r'<DT><STRONG>.*</STRONG></DT>', str)
print(match1)
print(match2)
print('-----------------------------------------------------------------')
for m in match1:
    print(m[7:-9])
print('----------------------------------')
for m in match2:
    print(m[12:-14])
