from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    majority_element = None
    count = 0

    for element in stream:
        if majority_element is None:
            count = 1
            majority_element = element
        elif element == majority_element:
            count += 1
        else:
            count -= 1

            if count == 0:
                majority_element = element
                count = 1
    return majority_element


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "majority_element.py",
            "majority_element.tsv",
            majority_search_wrapper,
        )
    )
