from typing import List
from collections import namedtuple

from test_framework import generic_test

Direction = namedtuple("Direction", ["x", "y"])
SHIFTS = [
    Direction(1, 0),
    Direction(0, -1),
    Direction(-1, 0),
    Direction(0, 1),
]


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    matrix = square_matrix
    depth = 0
    direction = 0
    res = []
    location = Direction(0, 0)

    while depth < len(matrix) // 2:
        for _ in range(4):
            for _ in range(depth, len(matrix) - depth - 1):
                res.append(matrix[location.x][location.y])
                location.x += SHIFTS[direction].x
                location.y += SHIFTS[direction].y
            direction = (direction + 1) % 4
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
