from list_node import ListNode
from test_framework import generic_test
from typing import List


def length(L: ListNode) -> int:
    """Return the length of a list. A null list has a length of 0.
    """
    if not L:
        return 0

    l = 0

    while L:
        l += 1
        L = L.next
    return l


def reverse(L: ListNode) -> ListNode:
    """Reverse a given linked list

    param L: The head of the linked list to reverse
    returns: The head of the new reversed linked list
    """
    # The sentinel head
    head = ListNode()
    it = L

    # This will traverse the list and insert each element at the beginning of
    # the linked list, which effectively reverses it.
    while it:
        next_node = it.next  # the next node we're going to iterate to
        tmp = head.next  # the current head of the list
        head.next = it  # insert the current node (it) as the head of the list
        it.next = tmp  # make the node after the head the previous head
        it = next_node  # progress the iterator

    return head.next


def ll_to_array(L: ListNode) -> List:
    it = L
    res = []

    while it:
        res.append(it.data)
        it = it.next
    return res


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True

    fast, slow = L, L

    # This gets 'slow' to the halfway point
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    first_iter = L
    second_iter = reverse(slow)

    while first_iter and second_iter:
        if first_iter.data != second_iter.data:
            return False

        first_iter = first_iter.next
        second_iter = second_iter.next
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_palindromic.py",
            "is_list_palindromic.tsv",
            is_linked_list_a_palindrome,
        )
    )
