import requests
import lxml.html
import json
import url
from special_symbols import sp_symbols


def search(text=''):
    req = requests.post(url.url_search, data={f'query': {text}, 'category': '', 'page': ''}).content
    data = json.loads(req)
    if len(data['itemsHtml']) != 0:
        answer = []
        a = lxml.html.fromstring(data['itemsHtml'])
        href = a.xpath('//a[@class="search-results-items-offer-img__wrap"]/@href')
        img = a.xpath(
            '//a[@class="search-results-items-offer-img__wrap"]/img[@class="search-results-items-offer-img"]/@src')
        name = a.xpath('//div[@class="search-results-items-offer__desc"]/a/text()')
        art = a.xpath('//div[@class="search-results-items-offer__desc"]/p/text()')
        prise = a.xpath('//div[@class="search-results-items-offer__desc"]/div/text()')
        for i in range(len(href)):
            if len(img[i]) > 19:
                answer.append({'href': href[i],
                               'img': img[i],
                               'name': sp_symbols(name[i]),
                               'art': sp_symbols(art[i]),
                               'prise': sp_symbols(prise[i])
                               })
            else:
                answer.append({'href': href[i],
                               'img': 'https://www.fpl.kz/media/img/noimage2_2EhtPP2.png',
                               'name': sp_symbols(name[i]),
                               'art': sp_symbols(art[i]),
                               'prise': sp_symbols(prise[i])
                               })
        return answer
    else:
        return
