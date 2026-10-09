from linked_list import LinkedList


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit = limit
        self.cache = {}
        self.order = LinkedList()

    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        value = node.value[1]

        # Move the accessed item to the head.
        self.order.remove(node)
        new_node = self.order.push_head(node.value)
        self.cache[key] = new_node

        return value

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.order.remove(node)

        elif len(self.cache) >= self.limit:
            # Remove the least recently used item.
            lru_item = self.order.pop_tail()
            del self.cache[lru_item[0]]

        # Add the item to the head as most recently used.
        node = self.order.push_head((key, value))
        self.cache[key] = node