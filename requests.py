import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
