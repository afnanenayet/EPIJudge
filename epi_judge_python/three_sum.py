from test_framework import generic_test


def has_three_sum(A, t):
    """ Given an array and some number `t`, determine whether there are three
    numbers that add up to t. Numbers can be used more than once.

    This can be solved by deconstructing the problem into the two sum problem.
    Sort the array, A, then loop through it. Then solve the two sum problem
    for A and t - (the iterated number).

    The two sum problem can be solved by sorting the array, then having two
    pointers at either end, i and j. If A[j] + A[i] < t, then iterate i down.
    Otherwise, iterate j up. This is an O(n) solution.

    Sorting is presumably O(n log(n)).

    Because we are iterating n times on an O(n) procedure, the time complexity
    is O(n^2).

    Note, this problem is solved assuming we can use each element in the array
    once, not with redundant usage of each element.
    """
    A = sorted(A)

    def has_two_sum(A, t):
        start, end = 0, len(A) - 1

        while start < end:
            if A[start] + A[end] < t:
                start += 1
            elif A[start] + A[end] > t:
                end -= 1
            else:
                return True
        return False

    for num in A:
        if has_two_sum(A, t - num):
            return True
    return False


if __name__ == "__main__":
    exit(generic_test.generic_test_main("three_sum.py", "three_sum.tsv", has_three_sum))
