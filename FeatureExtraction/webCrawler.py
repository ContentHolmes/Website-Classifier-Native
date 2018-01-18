import requests
from bs4 import BeautifulSoup

urls = ["http://www.performanceschool.org","http://www.directionjournal.com/"]
for url in urls:
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    metas = soup.find_all('meta')
    title = soup.find_all('title')

    for meta in metas:
        if 'name' in meta.attrs:
            if meta.attrs['name'] == 'description':
                print('description')
                print(meta.attrs['content'])
                
            if meta.attrs['name'] == 'keywords':
                print('keywords')
                print(meta.attrs['content'])
                
        if 'property' in meta.attrs:
            if meta.attrs['property'] == 'og:description':
                print('d2')
                print(meta.attrs['content'])
                
            if meta.attrs['property'] == 'og:keywords':
                print('k2')
                print(meta.attrs['content'])
        print("title",title[0].string)