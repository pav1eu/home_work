import json
import os
import pprint


def transaction_data(operation_json: str) -> list[dict]:
    try:
        with open(operation_json, encoding='UTF-8') as transaction:
            transaction_json = json.load(transaction)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    return transaction_json


project_root = os.path.dirname(os.path.dirname(__file__))
operations_path = os.path.join(project_root, 'data', 'operations.json')

if __name__ == '__main__':
    pprint.pprint(transaction_data(operations_path))
