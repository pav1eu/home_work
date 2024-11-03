from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(card_or_account_number: str) -> str:
    """Эта функция принимает на вход номер карты или счета и возвращает его маску."""
    if 'Счет' in card_or_account_number:
        list_of_symbols = ''.join(card_or_account_number)
        number = ''
        for symbols in list(list_of_symbols):
            if symbols.isdigit():
                number += symbols
        number = get_mask_account(number)
        return f'Счет {number}'
    else:
        list_of_symbols = ''.join(card_or_account_number)
        number = ''
        for symbols in list(list_of_symbols):
            if symbols.isdigit():
                number += symbols
        number = get_mask_card_number(number)
        return f'{card_or_account_number[0:-16]}{number}'

print(mask_account_card('Счет 73654108430135874305'))
print(mask_account_card('Visa Platinum 7000792289606361'))