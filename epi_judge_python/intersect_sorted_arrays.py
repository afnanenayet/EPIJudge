from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    res = list()
    it_a, it_b = 0, 0

    while it_a < len(A) and it_b < len(B):
        if A[it_a] == B[it_b]:
            if len(res) == 0 or A[it_a] != res[-1]:
                res.append(A[it_a])
            it_a += 1
            it_b += 1
        elif A[it_a] < B[it_b]:
            it_a += 1
        else:
            it_b += 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
