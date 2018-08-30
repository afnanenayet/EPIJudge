from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    """ Use a dictionary/counter to get a count of each character in the
    magazine. Deplete that counter while we scan characters from the letter,
    if we run out of letters or can't find a letter, then we fail. Otherwise,
    we can write the letter.

    N = number of characters in `letter_text`
    M = number of characters in `magazine_text`

    complexity:
        space: O(M)
        time: O(M + N)
    """
    # create a dict with the count of each letter in the string from magazine
    # text
    char_count = Counter(magazine_text)

    # check if for each character in the letter, we have enough characters
    # from the magazine, and that we have the character in the first place
    for character in letter_text:
        # If we don't have the character, can't write the letter. Terminate
        # early
        if character not in char_count:
            return False

        # we have used a char from the magazine, we need to indicate that using
        # the hash table
        char_count[character] -= 1

        # setting count to 0 does not remove it from the counter, we have to
        # manually delete it
        if char_count[character] == 0:
            del char_count[character]
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
