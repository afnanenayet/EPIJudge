import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    if len(A) == 0:
        return None

    root_idx = len(A) // 2
    root = A[root_idx]
    left_list = A[:root_idx]
    right_list = A[root_idx + 1:]
    left_subtree = build_min_height_bst_from_sorted_array(left_list)
    right_subtree = build_min_height_bst_from_sorted_array(right_list)
    return BstNode(root, left_subtree, right_subtree)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
