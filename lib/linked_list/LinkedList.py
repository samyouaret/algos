class LinkedListNode:
    value = None
    next = None

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.current = None

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

    def pop(self):
        if (self.head.next == None):
            val = self.head.value
            self.head = None
            return val

        temp = self.head
        while (temp.next.next != None):
            temp = temp.next
        val = temp.next.value
        temp.next = None

        return val

    def __iter__(self):
        self.current = self.head

        return self

    def __next__(self):
        if (self.current == None):
            raise StopIteration
        val = self.current.value
        self.current = self.current.next

        return val

    def __str__():
        list = []
        for value in list:
            list.append(value)

        return list.__str__()
