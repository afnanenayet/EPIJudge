import math
from typing import List
import bintrees

from test_framework import generic_test


class Pairing(object):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __gt__(self, other):
        return self.val > other.val


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    candidate = bintrees.RBTree([(Pairing(0, 0), None)])
    res = []

    while len(res) < k:
        min_pair, _ = candidate.pop_min()
        res.append(min_pair.val)
        candidate.insert(Pairing(min_pair.a + 1, min_pair.b), None)
        candidate.insert(Pairing(min_pair.a, min_pair.b + 1), None)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "a_b_sqrt2.py", "a_b_sqrt2.tsv", generate_first_k_a_b_sqrt2
        )
    )
