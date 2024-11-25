from typing import Union


def filter_by_currency(transitions: Union[list[dict]] , currency: str) -> Union[list[dict]]:
    """
    Функция должна возвращать итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    if transitions == []:
        return 'Список транзакций пустой'
    elif currency not in ['USD', 'RUB']:
        raise SyntaxError('Валюта не найдена. ')
    for some_trasition in transitions:
        if some_trasition['oprationAmount']['currency']['code'] == currency:
            yield some_trasition
    return iter([])