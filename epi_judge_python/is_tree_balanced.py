from test_framework import generic_test
from collections import namedtuple

BalanceRes = namedtuple("BalanceRes", ("bal", "height"))


def is_balanced_helper(node) -> BalanceRes:
    """ This is a helper function that returns a tuple containing both whether
    the subtree is valid and the height of the subtree. We split this out to a
    separate wrapper function because the main function only returns a tuple
    and must keep its function signature.

    complexity:
        space: O(N)
        time:  O(N)
    """
    # base case
    if not node:
        return BalanceRes(True, -1)

    # early termination so we don't have to traverse the whole tree when we
    # reach a failure point
    l_res = is_balanced_helper(node.left)

    if not l_res.bal:
        return BalanceRes(False, 0)

    r_res = is_balanced_helper(node.right)

    if not r_res.bal:
        return BalanceRes(False, 0)

    height_bal = abs(l_res.height - r_res.height) <= 1
    return BalanceRes(height_bal, max(l_res.height, r_res.height) + 1)


def is_balanced_binary_tree(tree) -> bool:
    res = is_balanced_helper(tree)
    return res.bal


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_balanced.py", "is_tree_balanced.tsv", is_balanced_binary_tree
        )
    )
