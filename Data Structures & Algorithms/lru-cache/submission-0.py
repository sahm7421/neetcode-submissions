class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Dummy nodes: left = LRU, right = most recent
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Node ko list se remove karo
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Node ko right dummy node ke theek pehle insert karo (Most Recent)
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # Access hua hai, toh isko most recent banao
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # Agar capacity exceed ho gayi to LRU node (left.next) remove karo
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]