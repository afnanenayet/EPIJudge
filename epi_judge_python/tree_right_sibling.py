import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    def process_level(node: BinaryTreeNode) -> None:
        """Process all of the nodes in a given level.

        Given the starting node for a level (which is the leftmost node),
        fill in the `node.next` field for every node in the level.

        param node: The starting node for the level
        """
        while node and node.left and node.right:
            # `next` for the left subtree is just the right subtree
            node.left.next = node.right

            # First we check that this isn't the last node for the level. If it
            # isn't, then we set the right sibling of the right child to the left
            # child of the node directly to the right of the current node (`node`).
            if node.next:
                node.right.next = node.next.left
            node = node.next

    # Traverse each level by descending to the left
    while tree and tree.left:
        process_level(tree)
        tree = tree.left


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = (
        clone_tree(original.left),
        clone_tree(original.right),
    )
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [
        [n.data for n in traverse_next(level)]
        for level in traverse_left(cloned)
    ]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "tree_right_sibling.py",
            "tree_right_sibling.tsv",
            construct_right_sibling_wrapper,
        )
    )
