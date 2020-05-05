from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    res = ''
    is_neg = x < 0

    if is_neg:
        x = x * -1

    while x > 0:
        current_digit = x % 10
        current_digit_str = str(current_digit)
        res = current_digit_str + res
        x = x // 10

    if is_neg:
        res = '-' + res
    return res


def string_to_int(s: str) -> int:
    if len(s) == 0:
        return 0

    res = 0
    negation_factor = 1
    start_index = 0

    if s[0] == '+':
        start_index = 1
    elif s[0] == '-':
        start_index = 1
        negation_factor = -1

    for c in s[start_index:]:
        try:
            digit = int(c)
        except Exception as e:
            pass
        res = (res * 10) + digit
    return res * negation_factor


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('int_to_string')
    if string_to_int(s) != x:
        raise TestFailure('string_to_int')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
