from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None

    sentinel_head = ListNode(0, L)
    first = sentinel_head
    second = sentinel_head

    for _ in range(k):
        first = first.next

    # After this loop ends, first will be on the last node
    while first and first.next:
        first = first.next
        second = second.next

    second.next = second.next.next
    return sentinel_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "delete_kth_last_from_list.py",
            "delete_kth_last_from_list.tsv",
            remove_kth_last,
        )
    )
