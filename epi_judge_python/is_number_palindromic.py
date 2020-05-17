from test_framework import generic_test
import math


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True

    length = math.floor(math.log10(x))
    left, right = 0, length

    def digit_at(i: int) -> int:
        """Get the digit at the ith position of a number (as if it were a
        string).
        """
        return (x // (10 ** i)) % 10

    while left < right:
        if digit_at(left) != digit_at(right):
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
