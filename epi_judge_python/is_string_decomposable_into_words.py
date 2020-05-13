import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    last_length = [-1 for _ in range(len(domain))]

    for i in range(len(domain)):
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1

        # We haven't computed whether or domain[:i + 1] is a valid prefix
        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1: i + 1] in dictionary:
                    last_length[i] = i - j

    # -1 is our placeholder that indicates that domain[:i + 1] is *not** a
    # valid prefix
    if last_length[-1] == -1:
        return []

    # Otherwise, we were able to successfully break down the entire string
    # into dictionary words. We can work backwards and take the lengths of the
    # words that we solved for to split the domain string.
    index = len(domain) - 1
    res = []

    # Work our way backwards through our results
    while index >= 0:
        end = index + 1
        start = index + 1 - last_length[index]
        res.append(domain[start:end])
        index -= last_length[index]
    return res[::-1]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
