from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(heights: List[int]) -> int:
    stack = []
    curr_max = 0

    for index, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= height:
            cand_height = heights[stack.pop()]
            cand_width = index if not stack else (index - stack[-1] - 1)
            curr_max = max(curr_max, cand_height * cand_width)
        stack.append(index)
    return curr_max


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "largest_rectangle_under_skyline.py",
            "largest_rectangle_under_skyline.tsv",
            calculate_largest_rectangle,
        )
    )
