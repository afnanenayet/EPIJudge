from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self.head = 0
        self.tail = 0
        self.size = 0
        self.entries = [None] * capacity
        return

    def enqueue(self, x: int) -> None:
        if self.size == len(self.entries):
            # Keep it contiguous
            self.entries = (
                self.entries[self.head :]
                + self.entries[: self.head]
                + ([None] * len(self.entries))
            )
            self.head = 0
            self.tail = self.size - 1

        self.tail = (self.tail + 1) % len(self.entries)
        self.entries[self.tail] = x
        self.size += 1

    def dequeue(self) -> int:
        if self.size == 0:
            # Can't dequeue from an empty queue
            return -1
        element = self.entries[self.head]
        self.entries[self.head] = None
        self.head = (self.head + 1) % len(self.entries)
        self.size -= 1
        return element

    def size(self) -> int:
        return self.size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == "Queue":
            q = Queue(arg)
        elif op == "enqueue":
            q.enqueue(arg)
        elif op == "dequeue":
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result)
                )
        elif op == "size":
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "circular_queue.py", "circular_queue.tsv", queue_tester
        )
    )
