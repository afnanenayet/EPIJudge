from typing import List
from collections import namedtuple

from test_framework import generic_test


Coordinate = namedtuple("Coordinate", ["x", "y"])


def fill_surrounded_regions(board: List[List[str]]) -> None:
    """Find the W's that aren't enclosed, store them in a set, and then turn
    all of the OTHER W's into B's.

    This is easy -- just do a BFS, using all of the W's on any edge to
    initialize the queue
    """

    def init_queue() -> List[Coordinate]:
        """Initialize the queue for the BFS by combing the edges of the board
        for white cells to serve as the iniitalization for the BFS
        """
        q = []

        for i in range(len(board)):
            if board[i][0] == "W":
                q.append(Coordinate(i, 0))

            if board[i][len(board[i]) - 1] == "W":
                q.append(Coordinate(i, len(board[i]) - 1))

        for i in range(len(board[0])):
            if board[0][i] == "W":
                q.append(Coordinate(0, i))

            if board[len(board) - 1][i] == "W":
                q.append(Coordinate(len(board) - 1, i))
        return q

    def neighbors(c: Coordinate) -> List[Coordinate]:
        """Calculate the neighboring coordinates of a given coordinate
        """
        transforms = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = []

        for op in transforms:
            cand_neighbor = Coordinate(c.x + op[0], c.y + op[1])

            if (
                0 <= cand_neighbor.x < len(board) and
                0 <= cand_neighbor.y < len(board[cand_neighbor.x])
            ):
                res.append(cand_neighbor)
        return res

    queue = init_queue()

    # Uncontained is the set of visited cells that are accessible from the
    # edges of the search space
    uncontained = set()

    while queue:
        node = queue.pop(0)
        uncontained.add(node)

        for neighbor in neighbors(node):
            if neighbor not in uncontained:
                queue.append(neighbor)

    # Now that we know which cells are uncontained, we can paint the other ones
    # black
    for x in range(len(board)):
        for y in range(len(board[x])):
            c = Coordinate(x, y)

            if board[x][y] == "W" and c not in uncontained:
                board[x][y] = "B"


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
