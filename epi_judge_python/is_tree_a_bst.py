from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return helper(tree, float("-inf"), float("inf"))


def helper(node, min_val, max_val):
    if node is None:
        return True

    if not min_val <= node.data <= max_val:
        return False

    return helper(node.left, min_val, node.data) and helper(node.right, node.data, max_val)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
