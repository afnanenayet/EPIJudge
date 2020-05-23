from typing import List
import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []
    max_heap = []

    heapq.heappush(max_heap, (-A[0], 0))
    res = []

    for _ in range(k):
        # max_heap[0] is the largest element
        cand_idx = max_heap[0][1]
        res.append(-heapq.heappop(max_heap)[0])

        # append either the left or right child to the heap depending on which
        # one is has the larger value
        left_child_idx = 2 * cand_idx + 1
        right_child_idx = 2 * cand_idx + 2

        if left_child_idx < len(A):
            heapq.heappush(max_heap, (-A[left_child_idx], left_child_idx))

        if right_child_idx < len(A):
            heapq.heappush(max_heap, (-A[right_child_idx], right_child_idx))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare,
        )
    )
