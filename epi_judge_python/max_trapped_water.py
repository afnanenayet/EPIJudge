from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    if len(heights) < 2:
        return 0
    max_height = 0
    left, right = 0, len(heights) - 1

    while left < right:
        # The height is bounded by the lower of the two columns
        height = min(heights[left], heights[right])
        width = right - left
        max_height = max(max_height, height * width)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_height


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
