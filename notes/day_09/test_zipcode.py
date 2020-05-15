''' Unit test for zipcode '''
# Requirement for zipcode:
# - 5 characters long
# - all numbers
from zipcode import is_zipcode


def test_is_zipcode_returns_false_when_greater_than_five():
    ''' tests functionality '''
    assert not is_zipcode('abcdefg')


def test_is_zipcode_returns_false_when_less_than_five():
    ''' tests functionality '''
    assert not is_zipcode('a')


def test_not_zipcode_if_five_chars_but_not_all_digits():
    ''' test '''
    assert not is_zipcode('abcde')


def test_not_zipcode_if_all_digits_but_not_five_chars():
    ''' test '''
    assert not is_zipcode('1234')
    assert not is_zipcode('123456')
    assert not is_zipcode('')


def test_not_zipcode_if_it_is_a_float():
    ''' test '''
    assert not is_zipcode(12345.12)


def test_not_zipcode_if_it_is_a_dict():
    ''' test '''
    assert not is_zipcode({'name': 'Dean'})
