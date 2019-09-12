from sqlite3 import connect
from requests import request
from bs4 import BeautifulSoup

resq = request(url = 'https://kinogo.by/', method="get")

soup = BeautifulSoup(resq.text)

soup.find('h2', {'class':'zagolovki'}).text

[i.text for i in soup.find_all('h2', {'class':'zagolovki'})]


all_names = []
for i in range(1, 11):
    req = request(url = 'https://kinogo.by/page/' + str(i), method="get")
    soup = BeautifulSoup(req.text)
    all_names.extend([i.text for i in soup.find_all('h2', {'class':'zagolovki'})])

len(all_names)

url = "https://kinogo.by" + soup.find('div',{'class':'overlaytumb'}).find('img').get('src')

imgg = request(url = url, method='get')

with open('mykitay.png', 'wb') as file:
    file.write(imgg.content)

from os import makedirs

makedirs('myimgbs4')

url.split('/')[-1]

all_urls = []
for i in range(1, 11):
    req = request(url = 'https://kinogo.by/page/' + str(i), method="get")
    soup = BeautifulSoup(req.text)
    urls = ["https://kinogo.by" + i.find('img').get('src') for i in soup.find_all('div',{'class':'overlaytumb'})]
    all_urls.extend(urls)
    for u in urls:
        imgg = request(url = u, method='get')
        with open('myimgbs4/' + u.split('/')[-1], 'wb') as file:
            file.write(imgg.content)

resq= request(url = 'https://kinogo.by/page/3', method="get")
soup = BeautifulSoup(resq.text)

url = soup.find('span', {'class':'podrobnee'}).find('a').get('href')

resq= request(url = url, method="get")

soup = BeautifulSoup(resq.text)

soup.find('div', {'class':'fullimg'}).find('div').text.strip().split('\n')[0]

all_names[34]

with connect('mydb.db') as con:
    con.execute("""CREATE TABLE movies(name text, img_name text, path_img text)""")

with connect('mydb.db') as con:
    for url, name in zip(all_urls, all_names):
        img_name = url.split('/')[-1]
        con.execute("""INSERT INTO movies(name, img_name, path_img) values(?,?,?)""",(name, img_name, "myimgbs4/" + img_name))

with connect('mydb.db') as con:
    cur = con.cursor()
    cur.execute("""SELECT * FROM movies""")

for row in cur.fetchall():
    print(row)