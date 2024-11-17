from typing import Union


def filter_by_state(
    list_of_states: Union[list[dict[str, Union[str, int]]]], state: str = "EXECUTED"
) -> Union[list[dict[str, Union[str, int]]]]:
    """Функция принимает список словарей с необязательным аргументом (state),
    Если аргумент не указан в вызове функции, она принимает стандартный
    И возвращает список словарей отформатированный по 'state'"""
    list_with_state = []
    for dicts in list_of_states:
        if "state" in dicts:
            if dicts["state"] == state:
                list_with_state.append(dicts)
        else:
            raise SyntaxError('"state" не в списке сортировка невозможна')
    if len(list_with_state) == 0:
        return 'Операций не найдено'
    return list_with_state


def sort_by_date(
    list_of_states: Union[Union[list[dict[str, Union[str, int]]]]], type_of_sorting: bool = True
) -> Union[list[dict[str, Union[str, int]]]]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки,
    Если параметр не указан, сортировка будет производиться от большего к меньшему
    Возвращает новый отсортированный список"""
    for dicts in list_of_states:
        if "date" not in dicts:
            raise SyntaxError('Отсутствует одна дата, сортировка невозможна')
    sorted_list_by_date = sorted(list_of_states, key=lambda date: date["date"], reverse=type_of_sorting)
    return sorted_list_by_date


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 939719570,
                    "state": "CANCELED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ]
        )
    )

    print(
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",

                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ]
        )
    )
