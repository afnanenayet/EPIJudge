from test_framework import generic_test


def parity(x: int) -> int:
    is_even = 0
    while x > 0:
        x = x & (x - 1)
        is_even ^= 1
    return is_even


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
