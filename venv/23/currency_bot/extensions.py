import requests
import json

currencie = {
    'Доллар': 'USD',
    'Рубль': 'RUB',
    'Евро': 'EUR',
    'Юань': 'CNY',
    'Лира': 'TRY',
    'Гривна': 'UAH'
}


class APIException(Exception):
    pass


class CryptoConverter:

    @staticmethod
    def get_price(quote=str, base=str, amount=str):
        try:
            quote_ticker = currencie[quote]
        except KeyError:
            raise APIException(f'Я не знаю волюту "{quote}"'
                               f'\n\nПопробуй ешё раз\nПример ввода: Доллар Рубль 10')

        try:
            base_ticket = currencie[base]
        except KeyError:
            raise APIException(f'Я не знаю волюту "{base}" '
                               f'\n\nПопробуй ешё раз\nПример ввода: Доллар Рубль 10')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Мне кажется "{amount}" - это не цифра'
                               f'\n\nПопробуй ешё раз\nПример ввода: Доллар Рубль 10')

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковае валюты {quote}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticket}')
        total_base = round(json.loads(r.content)[base_ticket] * amount, 2)
        return total_base
