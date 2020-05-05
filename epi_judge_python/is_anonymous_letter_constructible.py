from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    bank = dict()

    for letter in letter_text:
        if letter not in bank:
            bank[letter] = 0
        bank[letter] += 1

    for letter in magazine_text:
        if letter in bank:
            if bank[letter] <= 1:
                del bank[letter]
            else:
                bank[letter] -= 1
    return len(bank) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
