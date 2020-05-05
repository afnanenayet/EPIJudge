from typing import List, Dict
from collections import namedtuple

from test_framework import generic_test


Entry = namedtuple("Entry", ["last_idx", "closest"])


def find_nearest_repetition(paragraph: List[str]) -> int:
    # The minimum distance between any pair of words seen as we iterate
    closest = float("inf")
    distances = dict()

    for i, word in enumerate(paragraph):
        if word not in distances:
            distances[word] = Entry(i, float("inf"))
        else:
            new_word_dist = i - distances[word].last_idx
            new_word_closest = min(new_word_dist, distances[word].closest)
            distances[word] = Entry(i, new_word_closest)
            closest = min(closest, new_word_dist)

    if closest == float("inf"):
        return -1
    return closest


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "nearest_repeated_entries.py",
            "nearest_repeated_entries.tsv",
            find_nearest_repetition,
        )
    )
