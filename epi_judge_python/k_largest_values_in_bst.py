from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    visited = []

    def backwards_traversal(node):
        if node is None:
            return

        if len(visited) >= k:
            return
        else:
            backwards_traversal(node.right)

            if len(visited) < k:
                visited.append(node.data)
                backwards_traversal(node.left)

    backwards_traversal(tree)
    return visited


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py",
            "k_largest_values_in_bst.tsv",
            find_k_largest_in_bst,
            test_utils.unordered_compare,
        )
    )
