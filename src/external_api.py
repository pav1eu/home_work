import os
import requests
from dotenv import load_dotenv



def currency_convert(current_transaction: dict) -> float | str:
    """Конвертирует валюту в рубли при необходимости"""
    currency_amount = current_transaction['operationAmount']['amount']
    currency_type = current_transaction['operationAmount']['currency']['name']
    try:
        if currency_type == 'RUB':
            return currency_amount
        elif currency_type in ['USD', 'EUR']:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_type}&amount={currency_amount}"
            response = requests.get(url, headers=headers)
            result = response.json()
            if response.status_code != 200:
                return "Ошибка при получении курса валюты"
            else:
                return round(result['result'], 2)
    except KeyError:
        return "Операция является некорректной"


load_dotenv('../.env')
API_KEY = os.getenv('API_KEY')
headers = {'apikey':API_KEY}


if __name__ == '__main__':
    transaction = {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    print(currency_convert(transaction))
