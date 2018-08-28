from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    is_neg = False
    s = ""

    if x < 0:
        is_neg = True
        x *= -1

    # special case if x is 0
    if x == 0:
        return "0"

    while x:
        d = x % 10
        s = str(d) + s
        x = x // 10

    if is_neg:
        s = "-" + s
    return s


def string_to_int(s: str) -> int:
    num = 0
    is_neg = False

    if s[0] == "-":
        s = s[1:]
        is_neg = True

    for i, c in enumerate(s):
        power = len(s) - i - 1
        num += int(c) * (10 ** power)

    if is_neg:
        num *= -1
    return num


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
