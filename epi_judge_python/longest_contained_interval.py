from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    s = set(A)
    max_length = float("-inf")

    for elem in A:
        if elem not in s:
            continue

        # The bounds for the current largest contained range that includes
        # `elem`
        lower_bound = elem
        upper_bound = elem

        # iterate up
        while upper_bound + 1 in s:
            upper_bound += 1
            s.remove(upper_bound)

        # iterate down
        while lower_bound - 1 in s:
            lower_bound -= 1
            s.remove(lower_bound)
        curr_max = (upper_bound - lower_bound) + 1
        max_length = max(max_length, curr_max)
    return max_length


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "longest_contained_interval.py",
            "longest_contained_interval.tsv",
            longest_contained_range,
        )
    )
