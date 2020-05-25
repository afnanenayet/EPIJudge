from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    # `max_length[i]` is the longest subarray in `A[:i]` up to,
    # and including `A[i]`
    max_length = [0 for _ in range(len(A))]

    for i, elem in enumerate(A):
        max_length[i] = 1 + max(
            [x for (j, x) in enumerate(max_length[:i]) if A[j] <= elem] + [0]
        )
    return max(max_length)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            "longest_nondecreasing_subsequence.tsv",
            longest_nondecreasing_subsequence_length,
        )
    )
