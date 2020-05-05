from test_framework import generic_test


ADD = "+"
SUBTRACT = "-"
MULTIPLY = "*"
DIVIDE = "/"
DELIMITER = ","

# A function dispatch table with tokens and binary operations
DISPATCH_TABLE = {
    ADD: lambda x, y: x + y,
    SUBTRACT: lambda x, y: x - y,
    MULTIPLY: lambda x, y: x * y,
    DIVIDE: lambda x, y: x // y,
}


def evaluate(expression: str) -> int:
    tokens = expression.split(DELIMITER)
    stack = []

    for token in tokens:
        if token in DISPATCH_TABLE:
            y = stack.pop()
            x = stack.pop()
            result = DISPATCH_TABLE[token](x, y)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "evaluate_rpn.py", "evaluate_rpn.tsv", evaluate
        )
    )
