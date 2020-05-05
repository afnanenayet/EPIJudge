from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(
    preorder: List[int], inorder: List[int]
) -> BinaryTreeNode:
    def helper(
        pre_order: List[int], in_order: List[int]
    ) -> Optional[BinaryTreeNode]:
        if len(pre_order) == 0 or len(in_order) == 0:
            return None
        root = pre_order[0]

        # find the root in the in_order list
        # Everything to the left of that index is the in-order traversal for
        # the left subtree, everything to the right is the traversal for the
        # right subtree
        in_order_root_idx = in_order.index(root)
        left_in_order = in_order[:in_order_root_idx]
        right_in_order = in_order[in_order_root_idx + 1 :]
        num_left_elements = in_order_root_idx

        # We also know that the root_idx - 1 elements are the left subtree
        # pre-order traversal, and the remainder are the right subtree
        # pre-order traversal
        left_pre_order = pre_order[1 : num_left_elements + 1]
        right_pre_order = pre_order[num_left_elements + 1 :]
        node = BinaryTreeNode(root)
        node.left = helper(left_pre_order, left_in_order)
        node.right = helper(right_pre_order, right_in_order)
        return node

    return helper(preorder, inorder)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_from_preorder_inorder.py",
            "tree_from_preorder_inorder.tsv",
            binary_tree_from_preorder_inorder,
        )
    )
