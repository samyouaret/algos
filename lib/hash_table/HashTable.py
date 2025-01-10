
# Components of a Hash Table
#     Hash Function: Converts a key into a valid array index.
#     Buckets: An array where data is stored.
#     Collision Handling: Methods to resolve conflicts when two keys hash to 
# the same index.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_key(self, key):
        """Simple hash function that works with strings and numbers"""
        if isinstance(key, int):
            return key % self.size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table"""
        index = self._hash_key(key)
        # Check if the key already exists
        #  loop through chain of (i, array of chain[existing_key, value(_)])
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                self.table[index][i] = (key, value)  # Update value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve value for given key"""
        index = self._hash_key(key)
        # Search in the chain
        for [existing_key, value] in self.table[index]:
            if existing_key == key:
                return value

        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table"""
        index = self._hash_key(key)
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' does not exist")
