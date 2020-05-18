from test_framework import generic_test


def snake_string(s: str) -> str:
    """Build each line separately
    """
    res = ""
    offsets = [1, 0, 3]
    intervals = [4, 2, 4]

    for offset, interval in zip(offsets, intervals):
        res += s[offset::interval]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
