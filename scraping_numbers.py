#using www.crummy.com/software/BeautifulSoup/bs4/doc/
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ').strip()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    sum += int(tag.contents[0])
    count += 1
print('Count', count)
print('Sum', sum)

