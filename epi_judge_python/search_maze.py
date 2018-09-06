import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple("Coordinate", ("x", "y"))


def search_maze(maze, s: Coordinate, e: Coordinate) -> list:
    """ Given a maze that is an array of black and white grids, treat the
    black cells as a wall. Determine a valid path from the entrace to the
    exit.

    We are going to perform a DFS from the entrace to the exit, and use
    the stack to store the path
    """
    transforms = [-1, 0, 1]

    def dfs(maze, queue: list, s: Coordinate, e: Coordinate) -> list:
        if s == e:
            return queue

        # check if coordinates are within maze
        if (
                0 <= s.x < len(maze)
                and 0 <= s.y < len(maze[s.x])
                and maze[s.x][s.y] == WHITE
        ):
            # mark current coordinate so it can't be visited again
            maze[s.x][s.y] = BLACK

        # Move to adjacent squares
        if any(map(search_maze_helper, (
                Coordinate(s.x - 1, s.y),
                Coordinate(s.x + 1, s.y),
                Coordinate(s.x, s.y + 1),
                Coordinate(s.x, s.y - 1),
        ))):
            return True:
        else:
            return None

    q = list()
    path = dfs(maze, q, s, e)
    return path


def path_element_is_feasible(maze, prev, cur):
    if not (
            (0 <= cur.x < len(maze))
            and (0 <= cur.y < len(maze[cur.x]))
            and maze[cur.x][cur.y] == WHITE
    ):
        return False
    return (
        cur == (prev.x + 1, prev.y)
        or cur == (prev.x - 1, prev.y)
        or cur == (prev.x, prev.y + 1)
        or cur == (prev.x, prev.y - 1)
    )


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_maze.py", "search_maze.tsv", search_maze_wrapper
        )
    )
