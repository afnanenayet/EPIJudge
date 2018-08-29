from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    """ Add each element from the sorted arrays to the heap so it can sort
    them, and we can iterate through an arbitrary number of arrays and end
    up with a sorted union
    """
    h = list()
    first_run = True
    res = list()

    iters = [iter(array) for array in sorted_arrays]
    finished = [False for _ in range(len(iters))]

    # add next element from each array to heap, extract min and add to the
    # result
    while not all(finished):
        for i, it in enumerate(iters):
            try:
                n = next(it)
                heapq.heappush(h, n)
            except StopIteration:
                finished[i] = True
        while h:
            res.append(heapq.heappop(h))
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_arrays_merge.py", "sorted_arrays_merge.tsv", merge_sorted_arrays
        )
    )
