from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    next = None
    res = []
    prev = None

    while tree:
        # Still traversing down
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                res.append(tree.data)
                next = tree.right or tree.parent
        # We just finished traversing the left subtree, record the current
        # element, move to the right subtree if possible, or move up
        elif prev is tree.left:
            res.append(tree.data)
            next = tree.right or tree.parent
        # We finished traversing the right subtree, which means we have hit
        # every element in this tree, move up
        else:  # prev is tree.right
            next = tree.parent
        prev, tree = tree, next
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_with_parent_inorder.py",
            "tree_with_parent_inorder.tsv",
            inorder_traversal,
        )
    )
