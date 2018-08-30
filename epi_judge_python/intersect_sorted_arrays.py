from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    """ Walk through both arrays, iterating up whichever array has has an
    element less than the other. If the elements match up, add them to the
    union.

    complexity:
        time: O(m + n)
        space: O(n) where n is the size of the larger array
    """
    idx_a, idx_b = 0, 0
    res = list()

    while idx_a < len(A) and idx_b < len(B):
        if A[idx_a] < B[idx_b]:
            idx_a += 1
        elif A[idx_a] > B[idx_b]:
            idx_b += 1
        else:
            tmp = A[idx_a]

            # only add to list if element is not equal to previous element
            # (avoiding duplicates)
            if idx_a == 0 or tmp != A[idx_a - 1]:
                res.append(tmp)
            idx_a += 1
            idx_b += 1
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "intersect_sorted_arrays.py",
            "intersect_sorted_arrays.tsv",
            intersect_two_sorted_arrays,
        )
    )
