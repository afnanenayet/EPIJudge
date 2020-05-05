import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: List[str]):
    # Reverse the string, O(n)
    s.reverse()

    # The boundaries for a sublist (word) to reverse
    start, end = 0, 0

    for i, c in enumerate(s):
        if c == " ":
            end = i - 1

            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            start = i + 1
    # Reverse the last word
    end = len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
