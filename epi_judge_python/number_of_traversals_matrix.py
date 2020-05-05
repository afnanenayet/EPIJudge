from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    cache = [[0] * m] * n

    def helper(x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 1
        elif cache[x][y] == 0:
            num_ways_left = 0 if x == 0 else helper(x - 1, y)
            num_ways_up = 0 if y == 0 else helper(x, y - 1)
            cache[x][y] = num_ways_left + num_ways_up
        return cache[x][y]

    return helper(n - 1, m - 1)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_traversals_matrix.py",
            "number_of_traversals_matrix.tsv",
            number_of_ways,
        )
    )
