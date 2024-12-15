from typing import Union
import logging
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
full_path_file = os.path.join(base_dir, "logs", "masks.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(full_path_file, encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s [%(funcName)s] - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Эта функция принимает на вход номер карты и возвращает ее маску."""
    logger.info("Начало операции")
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        if str_card_number.isdigit():
            mask_of_card = f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
            logger.info("Операция завершена")
            return mask_of_card
        else:
            error = "Формат не поддерживается"
            logger.error(error)
            return error


def get_mask_account(account_number: Union[int, str]) -> str:
    """Эта функция принимает на вход номер счета и возвращает его маску."""
    logger.info("Начало операции")
    str_account_number = str(account_number)
    if len(str_account_number) == 20:
        if str_account_number.isdigit():
            mask_of_account = f"**{str_account_number[-4:]}"
            logger.info("Операция завершена")
            return mask_of_account
        else:
            error = "Формат не поддерживается"
            logger.error(error)
            return error


if __name__ == "__main__":
    print("Маска номера карты:", get_mask_card_number(4111111111111111))
    print("Маска номера счёта:", get_mask_account("12345678912345678912"))
