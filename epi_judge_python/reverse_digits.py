from test_framework import generic_test


def reverse(x: int) -> int:
    res = 0
    neg_factor = 1

    if x < 0:
        x = -x
        neg_factor = -1

    while x > 0:
        last_digit = x % 10
        x = x // 10
        res = res * 10 + last_digit
    return res * neg_factor


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_digits.py", "reverse_digits.tsv", reverse
        )
    )
