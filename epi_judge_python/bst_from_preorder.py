from typing import List, Optional

from bst_node import BstNode

from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def helper(root_idx, lower_bound, upper_bound):
        if root_idx >= len(preorder_sequence):
            return None
        elif not lower_bound <= preorder_sequence[root_idx] <= upper_bound:
            return None
        root = preorder_sequence[root_idx]
        root_idx += 1
        return BstNode(
            root,
            helper(root_idx, lower_bound, root),
            helper(root_idx, root, upper_bound),
        )
    return helper(0, float("-inf"), float("inf"))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
