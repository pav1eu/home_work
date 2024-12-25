from typing import Any, Iterator


def filter_by_currency(transactions: list[dict] | Any, currency: str | Any) -> Iterator | Any:
    """
    Функция должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    if len(transactions) > 0:
        if currency not in ["USD", "RUB"]:
            raise TypeError("Валюта не найдена.")
        elif type(currency) is not str:
            raise TypeError("Ошибка типа данных")
        elif type(transactions) is not list:
            raise TypeError("Ошибка типа данных")
        for some_transactions in transactions:
            if some_transactions["operationAmount"]["currency"]["code"] == currency:
                yield some_transactions
    return list(transactions)


def transaction_descriptions(transactions: list[dict] | Any) -> Iterator:
    """Функция возвращает описания для транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров карт формата 'ХХХХ ХХХХ ХХХХ ХХХХ' в заданном числовом диапозоне"""
    if not isinstance(start, (int | float)) or not isinstance(stop, (int | float)):
        raise TypeError("Ошибка типа данных")
    for x in range(start, stop + 1):
        card_number = f"{x:016}"
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number


if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for i in range(3):
            print(next(usd_transactions))
    except StopIteration:
        print("Список пустой!")

    transaction = transaction_descriptions(transactions)
    try:
        for i in range(3):
            print(next(transaction))
    except StopIteration:
        print("Список пустой!")

    for card_number in card_number_generator(1, 5):
        print(card_number)
