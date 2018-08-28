from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple

# Note: you could make this more efficient by storing the count of each max
# element rather than storing duplicate numbers
StackElement = namedtuple("StackElement", ["num", "count"])


class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self):
        if self.empty():
            raise IndexError()
        return self.max_stack[-1]

    def pop(self):
        if self.empty():
            raise IndexError()

        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def push(self, x):
        self.stack.append(x)

        if len(self.max_stack) < 1 or x >= self.max_stack[-1]:
            self.max_stack.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
