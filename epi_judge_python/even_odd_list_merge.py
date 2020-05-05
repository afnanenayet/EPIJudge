from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return None
    # First node is 0, which is even
    even_head = ListNode(-1)
    odd_head = ListNode(-1)
    lists = [even_head, odd_head]
    current_list = 0
    it = L

    while it:
        lists[current_list].next = it
        lists[current_list] = lists[current_list].next

        # Toggle which list we're operating on
        current_list ^= 1
        it = it.next

    lists[1].next = None
    lists[0].next = odd_head.next
    return even_head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "even_odd_list_merge.py", "even_odd_list_merge.tsv", even_odd_merge
        )
    )
