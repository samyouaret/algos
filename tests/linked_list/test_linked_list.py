from lib.linked_list.LinkedList import LinkedList
import unittest


class LinkedListTest(unittest.TestCase):

    def test_add_new_value_when_list_empty(self):
        list = LinkedList()
        list.add(3)
        assert list.head.value == 3

    def test_add_new_value_when_list_not_empty(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        assert list.head.value == 1
        assert list.head.next.value == 2

    def test_itertion_over_the_list(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        result = []
        for value in list:
            result.append(value)

        assert sorted(result) == sorted(list)
