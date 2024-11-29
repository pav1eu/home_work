from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def currency_data() -> list[dict[str, Any]]:
    return [
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


def test_filter_by_currency(currency_data: list[dict]) -> None:
    result = filter_by_currency(currency_data, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(result) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_empty_list() -> None:
    result = filter_by_currency([], "USD")
    assert list(result) == []


def test_filter_by_currency_invalid_currency(currency_data: list[dict]) -> None:
    with pytest.raises(TypeError):
        list(filter_by_currency(currency_data, "EUR"))


def test_filter_by_currency_wrong_type(currency_data: list[dict]) -> None:
    with pytest.raises(TypeError):
        next(filter_by_currency(1, [4, 3, 2]))
    with pytest.raises(TypeError):
        next(filter_by_currency("some_string", 2))
    with pytest.raises(TypeError):
        next(filter_by_currency(currency_data, 2))
    with pytest.raises(TypeError):
        next(filter_by_currency(521, "USD"))


def test_transaction_descriptions(currency_data: list[dict]) -> None:
    descriptions = transaction_descriptions(currency_data)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_empty(currency_data: list[dict]) -> None:
    descriptions = transaction_descriptions([])
    assert list(descriptions) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (0, 1, "0000 0000 0000 0000"),
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
        (1000, 1001, "0000 0000 0000 1000"),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    generated_number = card_number_generator(start, stop)
    assert next(generated_number) == expected


def test_card_number_generator_range() -> None:
    generated_number = card_number_generator(1, 5)
    assert next(generated_number) == "0000 0000 0000 0001"
    assert next(generated_number) == "0000 0000 0000 0002"
    assert next(generated_number) == "0000 0000 0000 0003"
    assert next(generated_number) == "0000 0000 0000 0004"
    assert next(generated_number) == "0000 0000 0000 0005"
