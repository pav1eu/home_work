import pytest
from typing import Union
from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def list_with_state():
    return [
        {"id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",},
        {"id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",},]


def test_filter_by_state(list_with_state):
    assert (filter_by_state(list_with_state) ==
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",}])


@pytest.fixture()
def empty_finale_list():
    return [
        {"id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",},
        {"id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",},]


@pytest.fixture()
def list_for_sort():
    return [{'date': "2019-07-03T18:35:29.512364"},
            {'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date(list_for_sort):
    assert (sort_by_date(list_for_sort) ==
            [{'date': '2019-07-03T18:35:29.512364'}, {'date': '2019-07-03T18:35:29.512364'}])


def test_filter_without_state(empty_finale_list):
    assert filter_by_state(empty_finale_list) == 'Операций не найдено'


@pytest.mark.parametrize('lists, expected', [([
        {"id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",},
        {"id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",},], 'Операций не найдено'),
    ([
        {"id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",},
        {"id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",},],

    [{"id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",}])])


def test_filter_by_state_executed(lists, expected):
    assert filter_by_state(lists) == expected


def test_filter_by_state_raise_error():
    with pytest.raises(SyntaxError):
        filter_by_state([{"id": 1, "date": "2022-02-24T15:04:32.356870"}])


def test_sort_by_date_error(list_for_sort):
    with pytest.raises(SyntaxError):
        sort_by_date([{ "id": 41428829,
                        "state": "EXECUTED",},
                        {"id": 615064591,
                         "state": "CANCELED",
                         "date": "2018-10-14T08:21:33.419441",},])

