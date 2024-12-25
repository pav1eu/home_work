import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def list_with_state() -> list:
    return [
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
    ]


def test_filter_by_state(list_with_state: list) -> None:
    assert filter_by_state(list_with_state) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        }
    ]


@pytest.fixture()
def empty_finale_list() -> list:
    return [
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture()
def list_for_sort() -> list:
    return [{"date": "2019-07-03T18:35:29.512364"}, {"date": "2019-07-03T18:35:29.512364"}]


def test_sort_by_date(list_for_sort: list) -> None:
    assert sort_by_date(list_for_sort) == [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2019-07-03T18:35:29.512364"},
    ]


def test_filter_without_state(empty_finale_list: list) -> None:
    assert filter_by_state(empty_finale_list) == []


@pytest.mark.parametrize(
    "lists, expected",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "CANCELED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            [],
        ),
        (
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
            ],
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                }
            ],
        ),
    ],
)
def test_filter_by_state_executed(lists: list, expected: list) -> None:
    assert filter_by_state(lists) == expected


def test_sort_by_date_error(list_for_sort: list) -> None:
    with pytest.raises(KeyError):
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
