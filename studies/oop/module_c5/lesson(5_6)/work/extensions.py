import requests
import json

from config import LAYER_API_KEY, currencies


class APIException(Exception):
    pass


class Currency:
    @staticmethod
    def get_price(cur_from, cur_to, amount):

        base = find_value_by_keys(currencies, cur_from)
        if base not in currencies.values():
            raise APIException(f'Выбор только из доступных валют/values')

        quote = find_value_by_keys(currencies, cur_to)
        if base == quote:
            raise APIException(f'Нельзя конвертировать одинаковую валюту {base}')

        try:
            if isinstance(amount, str):
                amount = float(amount.replace(',', '.'))

        except ValueError:
            raise APIException(f'Вероятно вместо цифр введены текстовые символы: {amount}')

        if amount < 0:
            raise APIException(f'число в валюте не может быть отрицательной {amount}')

        params = {
            'amount': amount,
            'from': base,
            'to': quote
        }
        headers = {"apikey": LAYER_API_KEY}
        url = "https://api.apilayer.com/exchangerates_data/convert"
        response = requests.request("GET", url, headers=headers, params=params)
        resp = json.loads(response.content)
        result = resp['result']
        return round(result, 2)


def find_value_by_keys(sl, k):  # преобразование значения (ru -> en)
    value = None
    for key, val in sl.items():
        if key == k:
            value = val
            break
    return value



# obj = Currency()
# print(obj.get_price(cur_from='Доллар', cur_to='Рубль', amount=40))
