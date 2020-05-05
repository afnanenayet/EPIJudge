from test_framework import generic_test


# tokens
PAREN_OPEN = "("
PAREN_CLOSE = ")"
SQ_OPEN = "["
SQ_CLOSE = "]"
BRACK_OPEN = "{"
BRACK_CLOSE = "}"

TOKENS = set(
    [PAREN_OPEN, PAREN_CLOSE, SQ_CLOSE, SQ_OPEN, BRACK_OPEN, BRACK_CLOSE]
)

# A mapping of opening delimiters to their respective closing delimiters
OPEN_BRACKETS = {
    PAREN_OPEN: PAREN_CLOSE,
    SQ_OPEN: SQ_CLOSE,
    BRACK_OPEN: BRACK_CLOSE,
}


def is_well_formed(s: str) -> bool:
    stack = []

    for char in s:
        if char in OPEN_BRACKETS.keys():
            stack.append(OPEN_BRACKETS[char])
        elif char in TOKENS:
            if len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_parenthesization.py",
            "is_valid_parenthesization.tsv",
            is_well_formed,
        )
    )
