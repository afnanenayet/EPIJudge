from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    res = []

    def go(current: str, left_remaining: int, right_remaining: int) -> None:
        """Incrementally build a string of parenthesis.

        There are several rules at play here. For instance, we can't create a
        string that starts with ")" and have it be balanced. In general, there
        must always be less (or equal to) ")" characters than "(" characters in
        a given string.

        At each iteration, we can add a "(" or an ")" if it's valid. We can
        keep track of how many of each parenthesis are left to add in each call.

        param current: The current string as we build it out
        param left_remaining: The number of "(" characters left to add to the
        string
        param right_remaining: The number of ")" characters left to add to the
        string
        """
        if right_remaining == 0:
            res.append(current)

        if right_remaining > left_remaining:
            go(current + ")", left_remaining, right_remaining - 1)

        if left_remaining > 0:
            go(current + "(", left_remaining - 1, right_remaining)

    go("", num_pairs, num_pairs)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_balanced_parentheses.py",
            "enumerate_balanced_parentheses.tsv",
            generate_balanced_parentheses,
            test_utils.unordered_compare,
        )
    )
