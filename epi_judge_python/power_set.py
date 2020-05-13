from typing import List

from test_framework import generic_test, test_utils
import math as m


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    res = []

    # Iterate through each possible value of i, use the set bits to determine
    # which element should be included in this particular set
    for i in range(1 << len(input_set)):
        # Convert the bits into indices
        bits = i
        subset = []

        while bits:
            index = int(m.log2(bits & ~(bits - 1)))
            subset.append(index)
            bits &= bits - 1
        res.append(subset)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
