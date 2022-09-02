import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ').strip()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
count = int(input('Enter count: '))
position = int(input('Enter position: '))
tags = soup('a')
for i in range(count):
    print('Retrieving: ', url)
    url = tags[position - 1].get('href', None)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
print('Retrieving: ', url)
    
