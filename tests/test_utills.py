import pytest
from unittest.mock import patch, mock_open
from src.utills import transaction_data
import os

project_root = os.path.dirname(os.path.dirname(__file__))
operations_path = os.path.join(project_root, 'data', 'operations.json')


@pytest.fixture()
def transaction() -> dict:
    transaction = {'date': '2019-08-26T10:50:58.294041',
                   'description': 'Перевод организации',
                   'from': 'Maestro 1596837868705199',
                   'id': 441945886,
                   'operationAmount': {'amount': '31957.58',
                                       'currency': {'code': 'RUB', 'name': 'руб.'}},
                   'state': 'EXECUTED',
                   'to': 'Счет 64686473678894779589'}
    return transaction


def test_transaction_data(transaction: dict) -> None:
    result = transaction
    assert transaction_data(operations_path)[0] == result


@patch('builtins.open', new_callable=mock_open)
def test_transaction_data(transaction: dict) -> None:
    result = []
    assert transaction_data('dummy_path.json') == result
