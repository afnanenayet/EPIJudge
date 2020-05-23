from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    if not A:
        return False
    m = len(A)
    n = len(A[0])
    row_idx = 0
    col_idx = len(A[0]) - 1

    while 0 <= row_idx < m and 0 <= col_idx < n:
        if x == A[row_idx][col_idx]:
            return True
        elif x < A[row_idx][col_idx]:
            col_idx -= 1
        else:
            row_idx += 1
    return False


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_row_col_sorted_matrix.py",
            "search_row_col_sorted_matrix.tsv",
            matrix_search,
        )
    )
