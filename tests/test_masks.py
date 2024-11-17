import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.fixture()
def card_number():
    return str(4111111111111111)

@pytest.fixture()
def account_number():
    return '23333333333333333333'

def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == f"**{account_number[-4:]}"

@pytest.mark.parametrize('card_number, expected', [(4111111111111111, '4111 11** **** 1111'),
                                                  ('4111111111111113', '4111 11** **** 1113'),
                                                  ('4111111111111183', '4111 11** **** 1183')])
def test_get_mask_card_number_with_different_inputs(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_with_invalid_input():
    with pytest.raises(SyntaxError):
        get_mask_card_number('bbbbbbbbbbbbbbbb')


def test_get_mask_card_number_with_no_input():
    with pytest.raises(SyntaxError):
        get_mask_card_number('')


@pytest.mark.parametrize('account_number, expected', [('12345678912345678912', '**8912'),
                                                  ('12345678915645678912', '**8912'),
                                                  ('12345678912345673456', '**3456')])
def test_get_mask_card_number_with_different_inputs(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_number_with_invalid_input():
    with pytest.raises(SyntaxError):
        get_mask_account('bbbbbbbbbbbbbbbbbbbb')


def test_get_mask_account_number_with_no_input():
    with pytest.raises(SyntaxError):
        get_mask_account('')

