from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()

    for i, third in enumerate(A):
        target = t - third
        l, u = 0, len(A) - 1

        while l <= u:
            two_sum = A[l] + A[u]

            if two_sum < target:
                l += 1
            elif two_sum > target:
                u -= 1
            else:
                print(f"{A[l]}, {A[u]}, {A[i]}")
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
