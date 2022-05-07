import requests
import bs4

'''
result=requests.get('https://example.com/')
#print(result.text)
soup=bs4.BeautifulSoup(result.text,'lxml')
#print((soup))

print(soup.select('title')[0].getText())
print(soup.select('p')[0].getText())

response = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(response.text,'lxml')
for i in soup.select('.toctext'):
    print(i.getText())
    
response = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(response.text,'lxml')
#print(soup.select('.thumbinner'))

computer=soup.select('img')
for i in computer:
    if i['alt'] == 'Deep Blue.jpg':
        img_link = i['src']
        img_link=requests.get('https:' + img_link)
        f = open('my_computer.jpg','wb')
        f.write(img_link.content)         
'''

import requests
import bs4
import re

result = requests.get('https://books.toscrape.com/')
soup = bs4.BeautifulSoup(result.text,'lxml')

search_pattern_for_rating = re.compile(r'star-rating .*')
#result = re.search(search_pattern_for_rating)

for i in soup.select('.star-rating '):
    print(i['class'])







