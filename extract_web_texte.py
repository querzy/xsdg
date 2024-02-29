# -*- coding: utf-8 -*-

#Représentation de la date et de l'heure - ISO 8601      YYYY-MM-DD
#The parser in +NumPy 1.7 is quite strict about only accepting ISO 8601 dates, with a few +convenience extensions.

import requests
from bs4 import BeautifulSoup

#url = 'https://keys.lol/bitcoin/1'
#url = 'https://medium.com/@mycodingblog/get-telegram-notification-when-python-script-finishes-running-a54f12822cdc'
#url = 'https://stackabuse.com/reading-and-writing-csv-files-in-python/'
url='https://www.liteforex.com/blog/for-professionals/neowave-part-13-corrections-rules-to-identify-a-correction/?utm_source=twitter.com&utm_medium=social&utm_campaign=neowave.-part-13.-corrections.-rules-to'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = ['[document]','noscript','header','html','meta','head','input','script']

for t in text:
	if t.parent.name not in blacklist:
		output += '{} '.format(t)

print(output)


with open('New_web_text.txt','w',encoding='utf-8') as outfile :
	outfile.write(output)

outfile.close()