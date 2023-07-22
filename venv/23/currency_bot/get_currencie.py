import requests
import lxml.html
from bs4 import BeautifulSoup
import text

html = requests.get(text.url).content
tree = lxml.html.document_fromstring(html)

root = BeautifulSoup(html, 'html.parser')
el = root.find('tbody').find_all('tr', )
count = 0
while count <= len(el):
    xpath1 = f'/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody/tr[{count}]/td[2]/a'
    xpath2 = f'/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody/tr[{count}]/td[7]'
    title1 = tree.xpath(f'{xpath1}/text()')
    title2 = tree.xpath(f'{xpath2}/text()')
    print(title1, title2)

