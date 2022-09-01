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
        # 1. the list is empty
        if self.head == None:
            self.head = LinkedListNode(value)
            return
        # 2. list is not empty, insert at last
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = LinkedListNode(value)
