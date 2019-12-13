# Implementation of the Map ADT using closed hashing and a probe with
# double hashing.
from array import Array

# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value 

# Defines constants to represent the status of each table entry.
UNUSED = None
EMPTY = _MapEntry(None, None)

class Hashmap:
    # Creates an empty map instance.
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) // 2

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the given key.
    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None

    # Adds a new entry to the map if the key does not exist. Otherwise, the
    # new value replace the current value associated with the key.
    def add(self, key, value):
        if key in self:
            slot = self._findSlot(key, False)
            self._table[slot].value = value
        else :
            slot = self._findSlot(key, True)

            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self.rehash()
                return True

    # Returns the value associated with the key.
    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key."
        return self._table[slot].value

    # Removes the entry associated with the key.
    def remove(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key"
        self._table[slot] = None
        return True

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return _hashMapIter(self._table)

    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _findSlot(self, key, forInsert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)

        # Probe for the key.
        M = len(self._table)

        while True:
            if forInsert and \
               (self._table[slot] is UNUSED or self._table[slot] is EMPTY) :
                return slot
            elif not forInsert and \
                 self._table[slot] is not EMPTY:
                if self._table[slot] is UNUSED:
                    return None
                elif self._table[slot].key == key:
                    return slot
            else :
                slot = (slot + step) % M

    # Rebuilds the hash table.
    def _rehash(self):
        # Create a new larger table.
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)

        # Modify the size attributes.
        self._count = 0
        self._maxCount = newSize - newSize // 3

        # Add the keys from the original array to the new table.
        for entry in origTable:
            if entry is not UNUSED and entry is not EMPTY:
                slot = self._findSlot(key, True)
                self._table[slot] = entry
                self._count += 1

    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        return abs(hash(key) % len(self._table))

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)

class _hashMapIter:
    def __init__(self, table):
        self._table = table
        self._ndx = 0

    def __iter__(self):
        return self

    def __next__(self):
        # find key
        while self._ndx < len(self._table) and \
              (self._table[self._ndx] is UNUSED or \
               self._table[self._ndx] is EMPTY) :
            self._ndx += 1

        if self._ndx < len(self._table) :
            curKey = self._table[self._ndx].key
            self._ndx += 1

            return curKey
        else :
            raise StopIteration
