import requests
import json
from config import API_KEY, values_


class APIException(Exception):
    pass


class API:
    @staticmethod
    def get_price(base, quote, amount):
        if quote == base:
            raise APIException(f"Одинаковые валюты нельзя перевести! {base}")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Количество должно быть числом!")
        if amount < 0:
            raise APIException("Количество не может быть меньше нуля!")
        try:
            base_ticker = values_[base]
        except KeyError:
            raise APIException(f"Не удалось обработать {base}")
        try:
            quote_ticker = values_[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать {quote}")


        req = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_ticker}")
        total = json.loads(req.content)
        total = float(total['conversion_rates'][quote_ticker]) * float(amount)
        return total
