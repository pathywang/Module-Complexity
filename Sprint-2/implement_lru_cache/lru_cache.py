class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError

        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None

    def _remove_node(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

    def _add_to_tail(self, node):
        node.next = None
        node.previous = self.tail

        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        # Move node to the most-recently-used position
        if node is not self.tail:
            self._remove_node(node)
            self._add_to_tail(node)

        return node.value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # Updating an item counts as using it
            if node is not self.tail:
                self._remove_node(node)
                self._add_to_tail(node)

            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)

        if len(self.cache) > self.limit:
            lru_node = self.head

            self._remove_node(lru_node)
            del self.cache[lru_node.key]