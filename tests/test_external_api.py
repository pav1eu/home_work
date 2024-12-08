import pytest
from unittest.mock import patch
import requests
from src.external_api import currency_convert


@pytest.fixture
def transaction_rub() -> dict:
    return {
        "operationAmount":
            {"amount": "1.00", "currency":
                {"name": "RUB", "code": "RUB"
                 }
             }
    }


@pytest.fixture()
def transaction_usd() -> dict:
    return {
        "operationAmount":
            {"amount": "1.00", "currency":
                {"name": "USD", "code": "USD"
                 }
             }
    }


def test_currency_convert_rub(transaction_rub: dict) -> None:
    assert currency_convert(transaction_rub) == 1.00


@patch('requests.get')
def test_currency_convert(mock_get):
    mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 1}, 'info': {'timestamp': 1, 'rate': 1}, 'result': 1}
    assert currency_convert({
        "operationAmount":
            {"amount": "1.00", "currency":
                {"name": "USD", "code": "USD"
                 }
             }
    }) == 1.00

