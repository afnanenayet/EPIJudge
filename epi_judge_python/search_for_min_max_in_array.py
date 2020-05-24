import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple("MinMax", ("smallest", "largest"))


def min_max_pair(a: int, b: int) -> (int, int):
    """Return (smaller, larger).

    This will compare `a` and `b`, returning a tuple with the smaller element,
    then the larger element.

    param a: A number
    param b: A number
    returns: `(smaller, larger)`, where `smaller` is the smaller element
    between `a` and `b`, and `larger` is the larger element between the two.
    """
    if a < b:
        return a, b
    else:
        return b, a


def find_min_max(A: List[int]) -> MinMax:
    curr_min = float("inf")
    curr_max = float("-inf")

    for i in range(0, len(A) - 1, 2):
        cand_min, cand_max = min_max_pair(A[i], A[i + 1])
        curr_min = min(curr_min, cand_min)
        curr_max = max(curr_max, cand_max)

    if len(A) % 2 != 0:
        curr_min = min(curr_min, A[-1])
        curr_max = max(curr_max, A[-1])
    return MinMax(curr_min, curr_max)


def res_printer(prop, value):
    def fmt(x):
        return "min: {}, max: {}".format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            "search_for_min_max_in_array.tsv",
            find_min_max,
            res_printer=res_printer,
        )
    )
