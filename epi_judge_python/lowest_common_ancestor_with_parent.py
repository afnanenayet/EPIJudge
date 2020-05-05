import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(
    node_0: BinaryTreeNode, node_1: BinaryTreeNode
) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    def depth(node: BinaryTreeNode) -> int:
        """Return the depth of a binary tree node with pointers to its parent.
        This will iterate up until the parent is found
        """
        it = node
        depth = 0

        if node is None:
            return depth

        while it:
            it = it.parent
            depth += 1
        return depth

    depth_0, depth_1 = depth(node_0), depth(node_1)
    lower_it, higher_it = node_1, node_0
    difference = abs(depth_1 - depth_0)

    if depth_0 < depth_1:
        lower_it, higher_it = node_0, node_1

    for _ in range(difference):
        if lower_it.parent:
            lower_it = lower_it.parent

    while lower_it is not higher_it and lower_it and higher_it:
        lower_it = lower_it.parent
        higher_it = higher_it.parent
    return lower_it


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(
            lca, must_find_node(tree, node0), must_find_node(tree, node1)
        )
    )

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_with_parent.py",
            "lowest_common_ancestor.tsv",
            lca_wrapper,
        )
    )
