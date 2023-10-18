import requests
import lxml.html
import json
import url

key = 'trixe'
answer = []

req = requests.post(url.url_search, data={f'query': {key}, 'category': '', 'page': ''}).content
data = json.loads(req)
a = lxml.html.fromstring(data['itemsHtml'])
href = a.xpath('//a[@class="search-results-items-offer-img__wrap"]/@href')
img = a.xpath('//a/img/@src')
name = a.xpath('//div[@class="search-results-items-offer__desc"]/a/text()')
art = a.xpath('//div[@class="search-results-items-offer__desc"]/p/text()')
prise = a.xpath('//div[@class="search-results-items-offer__desc"]/div/text()')

for i in range(len(href)):
    answer.append({'href': href[i],
                   'img': img[i],
                   'name': name[i],
                   'art': art[i],
                   'prise': prise[i]
                   })

for i in answer:
    print(i)
