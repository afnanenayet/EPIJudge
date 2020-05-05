import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # Using BFS
    q: List[Coordinate] = []
    visited = set()
    precedessor = dict()
    precedessor[s] = None
    q.append(s)
    max_y = len(maze[0])
    max_x = len(maze)

    while len(q) > 0:
        if q == e:
            break

        for neighbor in neighbors(q, max_x, max_y):
            is_valid_cell = maze[neighbor.x][neighbor.y] == WHITE

            if neighbor not in visited:
                precedessor[neighbor] = q
                q.append(neighbor)
    path = []
    path_it = e

    while path_it:
        path.insert(0, path_it)
        path_it = precedessor[path_it]
    return path


def neighbors(c: Coordinate, max_x: int, max_y) -> List[Coordinate]:
    """Generate a list of valid neighbor coordinates for a given 
    cell. All of the resulting coordinates will be within the board.
    """

    transformations = [-1, 1]
    res = []

    for x in transformations:
        for y in transformations:
            new_x = c.x + x
            new_y = c.y + y

            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                res.append(Coordinate(new_x, new_y))
    return res


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
        cur == (prev.x - 1, prev.y) or \
        cur == (prev.x, prev.y + 1) or \
        cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
