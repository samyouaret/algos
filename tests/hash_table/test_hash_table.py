
import unittest
from lib.hash_table.HashTable import HashTable


class HashTableTest(unittest.TestCase):
    def test_hash_table_insert(self):
        hash_table = HashTable(10)
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        self.assertEqual(hash_table.get("key1"), "value1")
        self.assertEqual(hash_table.get("key2"), "value2")

    def test_hash_table_delete(self):
        hash_table = HashTable(10)
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.delete("key1")
        self.assertEqual(hash_table.get("key1"), None)
        self.assertEqual(hash_table.get("key2"), "value2")
