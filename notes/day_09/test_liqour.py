''' Test '''
# Requirements:
# - Should return regular price if not a Vodka <-- Tested
# - Should be case insensitive when checking the name <-- Tested
# - Should return two dollars off if Vodka and day is Tuesday <-- Tested
# - Should return regular price if Vodka and day is not Tuesday <-- Tested
# - Today's day of the week should be case-insensitive <-- Tested

from liqour import Liqour


def test_if_not_vodka_type_then_always_regular_price_on_all_days():
    ''' test '''
    liqour_name = 'Jack Daniels'
    days_of_week = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday']

    regular_price = Liqour().get_regular_price(liqour_name)
    assert regular_price

    for day in days_of_week:
        price = Liqour().get_price(liqour_name, day)
        assert price == regular_price


def test_if_vodka_type_and_tuesday_then_returns_discount_price():
    ''' test '''
    liqour_name = 'Titos'
    day = 'Tuesday'

    regular_price = Liqour().get_regular_price(liqour_name)
    assert regular_price

    discount_amount = 2.00
    discount_price = regular_price - discount_amount
    assert Liqour().get_price(liqour_name, day) == discount_price


def test_if_vodka_type_and_not_tuesday_then_returns_regular_price():
    ''' test '''
    liqour_name = 'Titos'
    day = 'Wednesday'

    regular_price = Liqour().get_regular_price(liqour_name)
    assert regular_price

    assert Liqour().get_price(liqour_name, day) == regular_price


def test_if_vodka_different_case_and_tuesday_then_returns_discount_price():
    ''' test '''
    liqour_name = 'titos'
    day = 'Tuesday'

    regular_price = Liqour().get_regular_price(liqour_name)
    assert regular_price

    discount_amount = 2.00
    discount_price = regular_price - discount_amount
    assert Liqour().get_price(liqour_name, day) == discount_price


def test_if_vodka_day_or_week_different_case_and_tuesday_then_returns_discount_price():
    ''' test '''
    liqour_name = 'titos'
    day = 'tuesday'

    regular_price = Liqour().get_regular_price(liqour_name)
    assert regular_price

    discount_amount = 2.00
    discount_price = regular_price - discount_amount
    assert Liqour().get_price(liqour_name, day) == discount_price
