from LinkedList import LinkedList
import unittest


class LinkedListTest(unittest.TestCase):

    def test_add_new_value(self):
        list = LinkedList()
        list.add(3)
        assert list.head.value == 3


if __name__ == '__main__':
    unittest.main()
