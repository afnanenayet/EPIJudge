from typing import Iterator
from functools import reduce

from test_framework import generic_test
from test_framework.test_failure import TestFailure

TOTAL_BITS = 32
BUCKET_SIZE = 16


def find_missing_element(stream: Iterator[int]) -> int:

    # How many passes over the input we have to do
    num_passes = TOTAL_BITS // BUCKET_SIZE
    result = 0
    max_bucket_size = 1 << BUCKET_SIZE
    mask = reduce(
        lambda x, y: x | y,
        map(lambda x: 1 << x, [x for x in range(BUCKET_SIZE)]),
    )

    for current_pass in range(num_passes - 1, -1, -1):
        print(current_pass)
        missing_part = 0
        buckets = [0] * (1 << BUCKET_SIZE)

        for element in stream:
            index = (element >> (BUCKET_SIZE * current_pass)) & mask
            buckets[index] += 1

        min_idx = None
        current_min = buckets[0]
        for i, bucket in enumerate(buckets):
            if bucket < current_min:
                current_min = bucket
                min_idx = i

        if min_idx:
            result |= missing_part << (current_pass * BUCKET_SIZE)
    return result


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure("{} appears in stream".format(res))
    except ValueError:
        raise TestFailure("Unexpected no missing element exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "absent_value_array.py",
            "absent_value_array.tsv",
            find_missing_element_wrapper,
        )
    )
