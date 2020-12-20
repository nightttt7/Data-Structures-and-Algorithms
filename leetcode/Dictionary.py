# associative array, map, symbol table, or dictionary
# an abstract data type composed of a collection of (key, value) pairs
# such that each possible key appears at most once in the collection

# Implementation:


# Implementation 1. Hash table
class HashTable:
    def __init__(self):
        self.size = 11  # the maximum number that values could be put
        self.values = [None] * self.size
        self.keys = [None] * self.size

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, hash):
        return (hash+1) % self.size

    def __setitem__(self, key, value):
        hashvalue = self.hashfunction(key, self.size)
        while True:
            # no collision and new key
            if self.keys[hashvalue] is None:
                self.keys[hashvalue] = key
                self.values[hashvalue] = value
                break
            # no collision and existed key
            if self.keys[hashvalue] == key:
                self.values[hashvalue] = value
                break
            # collision
            hashvalue = self.rehash(hashvalue)

    def __getitem__(self, key):
        hashvalue = self.hashfunction(key, self.size)
        while True:
            # key not exist
            if self.keys[hashvalue] is None:
                raise KeyError('key not exist')
            # found
            if self.keys[hashvalue] == key:
                return self.values[hashvalue]
            # rehash
            hashvalue = self.rehash(hashvalue)


# h = HashTable()
# h[41] = 'a'
# h[58] = 'b'
# h[52] = 'c'
# h.keys
# h.values
# h[52]
# h[20]


# Implementation 2. Tree
# (1). Self-balancing binary search trees (common approach)
# see "Tree.py/Balanced Binary Search Trees"
# (2). unbalanced binary search tree
# see "Tree.py/Binary Search Trees"
