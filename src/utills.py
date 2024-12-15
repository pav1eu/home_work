import json
import logging
import os
import pprint
from typing import Any
from datetime import datetime


def transaction_data(operation_json: str) -> Any:
    """Возврщает транзакции из файла operations.json"""
    logger.info("Начало выполнение операции")

    try:
        with open(operation_json, encoding="UTF-8") as transaction:
            transaction_json = json.load(transaction)
    except FileNotFoundError as e:
        logger.error(f"{type(e).__name__}, не найден файл")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"{type(e).__name__}, пустой список")
        return []
    logger.info("Данные успешно получены")
    return transaction_json


project_root = os.path.dirname(os.path.dirname(__file__))
operations_path = os.path.join(project_root, "data", "operations.json")
full_path_file_logs = os.path.join(project_root, "logs", "utils.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(full_path_file_logs, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s [%(funcName)s] - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    pprint.pprint(transaction_data(operations_path))
