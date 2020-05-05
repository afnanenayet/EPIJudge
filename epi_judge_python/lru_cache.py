from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Node:
    """A node with references to it's predecessor and successor
    """

    def __init__(self, key=None, data=None, prev=None, n=None):
        self.prev = prev
        self.next = n
        self.data = data
        self.key = key


class LL:
    """A doubly linked list data structure, which provides accessors for the
    head and the tail of the list.
    """

    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def tail(self) -> Node:
        return self.tail

    def head(self) -> Node:
        return self._head


class LruCache:
    def __init__(self, capacity: int) -> None:
        self.d = dict()
        self.ll = LL()
        self.capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self.d:
            return -1
        node = self.d[isbn]
        self.delete_entry(node)
        self.update_entry(node)
        return node.data

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.d:
            prev_node = self.d[isbn]
            self.delete_entry(prev_node)

        if len(self.d) >= self.capacity:
            least_recently_used = self.ll.tail().prev
            lru_isbn = least_recently_used.key
            self.delete_entry(least_recently_used)
            del self.d[lru_isbn]
        node = Node(isbn, price)
        self.d[isbn] = node
        self.update_entry(node)

        if len(self.d) > self.capacity:
            pass
        return

    def erase(self, isbn: int) -> bool:
        node = self.d[isbn]
        self.delete_entry(node)
        del self.d[isbn]
        return True

    def update_entry(self, node: Node):
        """Insert a node at the head of the linked list
        """
        tmp = self.ll.head().next
        self.ll.head().next = node
        tmp.prev = node
        node.next = tmp
        node.prev = self.ll.head()

    def delete_entry(self, node: Node):
        """Delete (or more accurately, detach) an entry from the internal linked
        list
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != "LruCache":
        raise RuntimeError("Expected LruCache as first command")

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == "lookup":
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    "Lookup: expected " + str(cmd[2]) + ", got " + str(result)
                )
        elif cmd[0] == "insert":
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == "erase":
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    "Erase: expected " + str(cmd[2]) + ", got " + str(result)
                )
        else:
            raise RuntimeError("Unexpected command " + cmd[0])


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "lru_cache.py", "lru_cache.tsv", lru_cache_tester
        )
    )
