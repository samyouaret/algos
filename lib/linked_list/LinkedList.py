class LinkedListNode:
    value = None
    next = None

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedListNode(value)