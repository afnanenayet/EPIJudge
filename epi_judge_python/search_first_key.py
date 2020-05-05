from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l, u = 0, len(A) - 1

    while l <= u:
        i = (l + u) // 2

        if A[i] == k:
            u = i - 1

            if i == 0 or A[i - 1] < k:
                return i
        elif A[i] > k:
            u = i - 1
        else:
            l = i + 1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
