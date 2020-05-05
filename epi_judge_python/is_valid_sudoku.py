from typing import List

from test_framework import generic_test


def check_block(board: List[int]) -> bool:
    """Check whether a subset of a sudoku board is valid. A subset can be a
    row, a column, or a subarray.
    """
    if len(board) == 0:
        return True

    used = [False] * 9

    for i in board:
        if i != 0:
            if used[i - 1]:
                return False
            used[i - 1] = True
    return True


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for i in range(9):
        column = []
        row = []

        for j in range(9):
            column.append(partial_assignment[i][j])
            row.append(partial_assignment[j][i])

        if not check_block(column) or not check_block(row):
            return False

    # Flatten each subarray so we can use it with the `check_block` method
    for n in range(3):
        subarray = []

        for i in range(3):
            for j in range(3):
                x = (n * 3) + i
                y = (n * 3) + j
                subarray.append(partial_assignment[x][y])
        if not check_block(subarray):
            return False
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
