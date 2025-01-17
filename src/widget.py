from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Эта функция принимает на вход номер карты или счета и возвращает его маску."""
    if 'Счет' in card_or_account_number:
        list_of_symbols = ''.join(card_or_account_number)
        masked_number = ''
        for symbols in list(list_of_symbols):
            if symbols.isdigit():
                masked_number += symbols
        masked_number = get_mask_account(masked_number)
        return f'Счет {masked_number}'
    else:
        list_of_symbols = ''.join(card_or_account_number)
        masked_number = ''
        for symbols in list(list_of_symbols):
            if symbols.isdigit():
                masked_number += symbols
        masked_number = get_mask_card_number(masked_number)
        return f'{card_or_account_number[0:-16]}{masked_number}'


def get_date(correct_date: str) -> str:
    """Функция форматирует и возвращает дату в виде ДД.ММ.ГГГГ."""
    return f'{correct_date[8:10]}.{correct_date[5:7]}.{correct_date[0:4]}'


if __name__ == "__main__":
    print(mask_account_card('Счет 73654108430135874305'))
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(get_date("2024-03-11T02:26:18.671407"))
