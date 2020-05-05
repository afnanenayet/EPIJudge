from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    res = []

    def helper(idx):
        if idx == len(A):
            res.append(A)
            return

        for i in range(idx, len(A)):
            A[idx], A[i] = A[i], A[idx]
            helper(idx + 1)
            A[idx], A[i] = A[i], A[idx]

    helper(0)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "permutations.py",
            "permutations.tsv",
            permutations,
            test_utils.unordered_compare,
        )
    )
