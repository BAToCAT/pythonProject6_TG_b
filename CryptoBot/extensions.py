import requests
import json
from config import keys

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно конвертировать {base} в {base}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {quote}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неудалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = amount * json.loads(r.content)[keys[base]]
        return total_base
