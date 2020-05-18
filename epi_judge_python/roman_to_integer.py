from test_framework import generic_test
import functools

TOKENS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_integer(s: str) -> int:
    """Iterate through the string backwards, (right to left) and accumulate a
    running value. If the current value is less than the value of the next
    letter (to letter to the left), then subtract the current value from the
    next letter.
    """
    if not s:
        return 0

    res = TOKENS[s[-1]]

    for i in reversed(range((len(s) - 1))):
        curr = TOKENS[s[i]]
        next = TOKENS[s[i + 1]]

        if curr < next:
            res -= curr
        else:
            res += curr
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
