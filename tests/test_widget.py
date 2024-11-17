import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture()
def account_number() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture()
def card_number() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture()
def date() -> str:
    return "2024-03-11T02:26:18.671407"


def test_mask_if_account_number(account_number: str) -> None:
    assert mask_account_card(account_number) == "Счет **4305"


def test_mask_if_card_number(card_number: str) -> None:
    assert mask_account_card(card_number) == "Visa Platinum 7000 79** **** 6361"


def test_get_date_correct_format(date: str) -> None:
    assert get_date(date) == "11.03.2024"


@pytest.mark.parametrize(
    "account_or_card_number, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Pony Express 4444111122225555", "Pony Express 4444 11** **** 5555"),
    ],
)
def test_mask_account_card_different_inputs(account_or_card_number: str, expected: str) -> None:
    assert mask_account_card(account_or_card_number) == expected


def test_errors_in_mask_account_card_small_account_number() -> None:
    with pytest.raises(SyntaxError):
        mask_account_card("Счет 123123")


def test_errors_in_mask_account_card_symbols_in_card_number() -> None:
    with pytest.raises(SyntaxError):
        mask_account_card("Visa Platinum 70007922896063as")


def test_errors_in_mask_account_card_no_input() -> None:
    with pytest.raises(SyntaxError):
        mask_account_card("")


@pytest.mark.parametrize(
    "date, expected", [("2124-03-01T02:26:18.671407", "01.03.2124"), ("2124-12-99T02:26:18.671427", "99.12.2124")]
)
def test_get_date_different_inputs(date: str, expected: str) -> None:
    assert get_date(date) == expected


def test_errors_get_date_unexpected_symbol() -> None:
    with pytest.raises(SyntaxError):
        get_date("2124-03-01T02:26:18.671407x")


def test_error_get_date_not_enough_symbols() -> None:
    with pytest.raises(SyntaxError):
        get_date("2124-03-01T02:26:18")


def test_error_get_date_no_symvols() -> None:
    with pytest.raises(SyntaxError):
        get_date("")
