import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * level


class SkipList:
    MAX_LEVEL = 16

    def __init__(self):
        self.head = Node(None, self.MAX_LEVEL)
        self.level = 1

    def random_level(self):
        level = 1

        while (
            level < self.MAX_LEVEL
            and random.random() < 0.5
        ):
            level += 1

        return level

    def insert(self, value):
        update = [None] * self.MAX_LEVEL

        current = self.head

        for level in range(self.level - 1, -1, -1):
            while (
                current.next[level] is not None
                and current.next[level].value < value
            ):
                current = current.next[level]

            update[level] = current

        new_level = self.random_level()

        if new_level > self.level:
            for level in range(self.level, new_level):
                update[level] = self.head

            self.level = new_level

        node = Node(value, new_level)

        for level in range(new_level):
            node.next[level] = update[level].next[level]
            update[level].next[level] = node

    def contains(self, value):
        current = self.head

        for level in range(self.level - 1, -1, -1):
            while (
                current.next[level] is not None
                and current.next[level].value < value
            ):
                current = current.next[level]

        current = current.next[0]

        return (
            current is not None
            and current.value == value
        )
     
    def __contains__(self, value):
        return self.contains(value)



    