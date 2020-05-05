from typing import List

from test_framework import generic_test, test_utils

# TODO this is a lookup table of digits to a list of corresponding letters
LETTERS = {}


def phone_mnemonic(phone_number: str) -> List[str]:
    res = []

    def helper(i, current_phrase):
        """A helper method to generate a mnemonic for a phone number.

        param i: The index in the phone_number that we're currently working on
        param current_phrase: The current branch of the phrase that was built
        up for this current branch
        """
        if i == len(phone_number):
            res.append(current_phrase)

        for letter in LETTERS[phone_number[i]]:
            helper(i + 1, current_phrase + [letter])

    return []


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )
