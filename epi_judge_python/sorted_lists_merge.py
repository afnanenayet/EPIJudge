from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    head = ListNode()
    curr = head
    it_1, it_2 = L1, L2

    # special cases
    if L1 is None:
        return L2
    elif L2 is None:
        return L1

    # walk through each list, merging the lower entry
    while it_1 is not None and it_2 is not None:
        if it_1.data <= it_2.data:
            curr.next = it_1
            curr = curr.next
            it_1 = it_1.next
        else:
            curr.next = it_2
            curr = curr.next
            it_2 = it_2.next

    for it in [it_1, it_2]:
        while it is not None:
            curr.next = it
            it = it.next
            curr = curr.next
    return head.next


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_lists_merge.py", "sorted_lists_merge.tsv", merge_two_sorted_lists
        )
    )
