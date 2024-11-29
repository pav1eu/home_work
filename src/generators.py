from collections.abc import Iterator
from typing import Any, Union


def filter_by_currency(transactions: Union[list[dict[str, Any]]], currency: str) -> Iterator[dict[str, Any]]:
    """
    Функция должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    if len(transactions) > 0:
        if currency not in ['USD', 'RUB']:
            raise TypeError('Валюта не найдена.')
        elif type(currency) != str:
            raise TypeError('Ошибка типа данных')
        elif type(transactions) != list:
            raise TypeError('Ошибка типа данных')
        for some_transactions in transactions:
            if some_transactions['operationAmount']['currency']['code'] == currency:
                yield some_transactions
    return list(transactions)


if __name__ == '__main__':
    transactions = [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]
    usd_transactions = filter_by_currency(transactions, "USD")
    for i in range(1):
        print(next(usd_transactions))
