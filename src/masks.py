from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Эта функция принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number)
    if str_card_number.isdigit():
        mask_of_card = f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
        return mask_of_card
    else:
        return "Неверный формат номера карты"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Эта функция принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    if str_account_number.isdigit():
        mask_of_account = f"**{str_account_number[-4:]}"
        return mask_of_account
    else:
        return "Неверный формат номера счета"


if __name__ == "__main__":
    print(get_mask_card_number(str(input("Впишите номер карты: "))))
    print(get_mask_account('73654108430135874305'))
