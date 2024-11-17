from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Эта функция принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        if str_card_number.isdigit():
            mask_of_card = f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
            return mask_of_card
        else:
            raise SyntaxError("Неверный формат номера карты")
    else:
        raise SyntaxError("Неверный формат номера карты")


def get_mask_account(account_number: Union[int, str]) -> str:
    """Эта функция принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    if len(str_account_number) == 20:
        if str_account_number.isdigit():
            mask_of_account = f"**{str_account_number[-4:]}"
            return mask_of_account
        else:
            raise SyntaxError("Неверный формат номера счета")
    else:
        raise SyntaxError("Неверный формат номера счета")


if __name__ == "__main__":
    print("Маска номера карты:", get_mask_card_number(4111111111111111))
    print("Маска номера счёта:", get_mask_account('12345678912345678912'))

