from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    base = 10
    res = A

    for i in reversed(range(len(res))):
        new_digit = A[i] + carry
        carry = 0

        if new_digit >= base:
            carry = new_digit // base
            new_digit = new_digit % base
        res[i] = new_digit

        # Since res is a copy of A, once the carry is 0, we know that we're
        # done
        if carry == 0:
            return res

    # We might have to add a new digit to the beginning of the array
    if carry > 0:
        res.insert(0, carry)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_increment.py", "int_as_array_increment.tsv", plus_one
        )
    )
