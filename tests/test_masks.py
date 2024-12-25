import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def card_number() -> str:
    return str(4111111111111111)


@pytest.fixture()
def account_number() -> str:
    return "23333333333333333333"


def test_get_mask_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def test_get_mask_account(account_number: str) -> None:
    assert get_mask_account(account_number) == f"**{account_number[-4:]}"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (4111111111111111, "4111 11** **** 1111"),
        ("4111111111111113", "4111 11** **** 1113"),
        ("4111111111111183", "4111 11** **** 1183"),
    ],
)
def test_get_mask_card_number_with_different_inputs(card_number: str | int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected
