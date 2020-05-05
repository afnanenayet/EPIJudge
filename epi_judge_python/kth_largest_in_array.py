from typing import List
import random

from test_framework import generic_test


def partition(A: List[int], pivot_idx: int, start: int, end: int) -> int:
    """Partition a subset of an array around a pivot. Returns the index of the
    new pivot.
    """
    A[pivot_idx], A[start] = A[start], A[pivot_idx]
    pivot_idx = start
    pivot = A[pivot_idx]

    i = start + 1
    j = start + 1

    while j < end:
        elem = A[j]
        if elem > pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1
    A[i], A[pivot_idx] = A[pivot_idx], A[i]
    pivot_idx = i
    return pivot_idx


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    l = 0  # lower bound index (left)
    u = len(A) - 1  # upper bound index (right)
    k_index = 0

    while l <= u:
        pivot_idx = random.randint(l, u)
        pivot_idx = partition(A, pivot_idx, l, u)

        if pivot_idx < k - 1:
            l = pivot_idx + 1
        elif pivot_idx == k - 1:
            return A[pivot_idx]
        else:
            u = pivot_idx - 1
    return A[pivot_idx]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "kth_largest_in_array.py",
            "kth_largest_in_array.tsv",
            find_kth_largest,
        )
    )
