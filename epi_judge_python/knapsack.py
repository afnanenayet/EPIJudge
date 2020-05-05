import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple("Item", ("weight", "value"))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    cache = [[None] * capacity] * len(items)

    # base case
    cache[0][0] = 0

    for i in range(len(items)):
        for w in range(capacity):
            if i == 0 or w == 0:
                cache[i][w] = 0
                continue

            # Get the maximum value we can get if we select this item, or if we
            # don't select this item
            if items[i].weight > w:
                cache[i][w] = cache[i - 1][w]
            else:
                cache[i][w] = max(
                    cache[i - 1][w],
                    cache[i - 1][w - items[i].weight] + items[i].value,
                )
    return cache[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity)
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "knapsack.py", "knapsack.tsv", optimum_subject_to_capacity_wrapper
        )
    )
