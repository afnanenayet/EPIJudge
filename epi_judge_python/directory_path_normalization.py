import string

from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return ""

    stack = []

    if path[0] == "/":
        stack.append("/")

    for token in [token for token in path.split("/") if token not in [".", ""]]:
        if token == "..":
            if not stack or stack[-1] == "..":
                stack.append(token)
            else:
                stack.pop()
        else:
            stack.append(token)

    interpersed = "/".join(stack)
    if interpersed.startswith("//"):
        return interpersed[1:]
    return interpersed


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "directory_path_normalization.py",
            "directory_path_normalization.tsv",
            shortest_equivalent_path,
        )
    )
