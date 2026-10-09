class Node:
     __slots__ = ("value", "next", "previous")

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        return node

    def pop_tail(self):
        node = self.tail

        if node is None:
            return None

        self.remove(node)

        return node.value

    def remove(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = node.next
            self.head.previous = None

        elif node == self.tail:
            self.tail = node.previous
            self.tail.next = None

        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.next = None
        node.previous = None