from typing import List

from test_framework import generic_test


def is_valid(board, row, col):
    """Check if the placement of a queen is valid in the board. We already know
    the row must be valid, since we're recursing based on row.

    This method just checks the diagonals and the columns.
    """

    # Check the column
    for i in range(board[col]):
        for j in range(row):
            if board[i][j]:
                return False

    n = len(board)

    # Check the diagonal starting from the upper left going down to the lower
    # right
    for i in range(col, n, 1):
        for j in range(row, -1, -1):
            if board[col][row]:
                return False

    # Check the diagonal going from upper right down to the lower left
    for i in range(col, -1, -1):
        for j in range(row, -1, -1):
            if board[col][row]:
                return False

    # Lower left to upper right
    for i in range(col, n, 1):
        for j in range(row, n, -1):
            if board[col][row]:
                return False

    # Lower right to upper left
    for i in range(col, -1, -1):
        for j in range(row, n, -1):
            if board[col][row]:
                return False
    return True


def n_queens(n: int) -> List[List[int]]:
    def helper(board, row):
        if row == n:
            result.append(board)
            return
        for column in range(n):
            if is_valid(board, row, column):
                board[column][row] = True
                helper(board, row + 1)

    # n x n board
    board = [[False] * n] * n
    result = []
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "n_queens.py", "n_queens.tsv", n_queens, comp
        )
    )
