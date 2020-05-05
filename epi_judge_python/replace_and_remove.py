import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    write_index = 0
    a_count = 0

    for i, c in enumerate(s):
        if c != 'b':
            s[write_index] = s[i]
            write_index += 1
        if c == 'a':
            a_count += 1

    print(s)

    final_size = write_index + a_count
    back_index = final_size - 1

    for i in range(write_index - 1, -1, -1):
        if s[i] == 'a':
            s[back_index] = 'd'
            back_index -= 1
            s[back_index] = 'd'
        else:
            s[back_index] = s[i]
        back_index -= 1
    return final_size - 2


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
