from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    def helper(node_0, node_1) -> bool:
        if not node_0 and not node_1:
            return True
        elif node_0 and node_1:
            return (
                node_0.data == node_1.data
                and helper(node_0.left, node_1.right)
                and helper(node_0.right, node_1.left)
            )
        # This means that either node_0 (exclusive or) node_1 is null
        return False

    if not tree:
        return True

    return helper(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
