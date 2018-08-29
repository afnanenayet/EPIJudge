from test_framework import generic_test


def search_first_of_k(A, k):
    L, R = 0, len(A) - 1

    while L <= R:
        # with Python's "big" integers, don't need to worry about buffer 
        # overflow bug
        M = (L + R) // 2

        if A[M] > k:
            R = M - 1
        elif A[M] < k:
            L = M + 1
        # everything below this has the condition A[M] == k
        elif M == 0 or A[M - 1] != k:
            return M
        else:
            R = M - 1
    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", "search_first_key.tsv", search_first_of_k
        )
    )
