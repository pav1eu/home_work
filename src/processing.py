from typing import Union


def filter_by_state(list_of_dicts: Union[list], state="EXECUTED") -> list:
    """Функция принимает список словарей с необязательным аргументом (state),
    Если аргумент не указан в вызове функции, она принимает стандартный
    И возвращает список словарей отформатированный по 'state'"""
    list_with_state = []
    for dicts in list_of_dicts:
        if "state" in dicts:
            if dicts["state"] == state:
                list_with_state.append(dicts)
    return list_with_state


def sort_by_date(list_of_dicts: Union[list], reverse="True") -> list:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки,
    Если параметр не указан, сортировка будет производиться от большего к меньшему
    Возвращает новый отсортированный список"""
    sorted_list = sorted(list_of_dicts, key=lambda date: date["date"], reverse=reverse)
    return sorted_list


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
                    "state": "EXECUTED",
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
                    "date": "2018-10-14T08:21:33.419441",
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
