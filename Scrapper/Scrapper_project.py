import requests
import bs4
import re
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.3twe7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=ca)

result = requests.get('https://books.toscrape.com/')
soup = bs4.BeautifulSoup(result.text,'lxml')

booklist = []

pg = 1
next_page=True
search_pattern_for_rating = re.compile(r'star-rating .*')
books_rating = {}

while next_page:

    result = requests.get('https://books.toscrape.com/catalogue/page-' + str(pg) + '.html')
    soup = bs4.BeautifulSoup(result.text,'lxml')
    for i,j in zip(soup.select('img'),soup.select('.star-rating ')):
        books_rating[i['alt']]=j['class'][1]
        booklist.append(i['alt'])

    pg = pg+1
    if not soup.select('.next'):
        next_page = False

j=len(booklist)

scapper_db = client['testdb']
ratings_table = scapper_db['Books_&_their_rating']

l=[]

for k,v in books_rating.items():
    l.append({k:v})

ratings_table.insert_many(l)


'''
for i in booklist:
    book_name = f'{i}_{j}'
    book_name = book_name.split()
    book_name = '-'.join(book_name)
    result = requests.get(f'https://books.toscrape.com/catalogue/{book_name}/index.html')
    print(book_name,result.status_code)

    j=j-1
    
'''




