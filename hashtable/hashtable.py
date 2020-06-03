class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        r = f"({self.value})"
        cur = self.next
        while cur is not None and cur.next is not None:
            r += f" -> ({cur.next.value})"
            cur = cur.next
        return r
    # def __str__(self):
    #     return f"HashTableEntry(   {repr(self.key)} , {repr(self.value)}  )"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = max(MIN_CAPACITY, capacity)
        self.table = [None] * self.capacity
        self.population = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.population / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        prime = 0x100000001b3
        offset = 0xcbf29ce484222325
        hash = offset
        str_bytes = key.encode()
        for c in str_bytes:
            hash = (hash * prime) ^ c
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        str_bytes = key.encode()
        hash = 5381
        for c in str_bytes:
            hash = ((hash << 5) + hash) + c
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        lf = self.get_load_factor()
        if lf > 0.7:
            self.resize(self.capacity * 2)
            print(f"resize capacity from {lf} to {self.get_load_factor()}")
        elif lf < 0.2:
            if self.capacity < 16:
                self.resize(self.capacity // 2)
                print(
                    f"resize capacity from {lf} to {self.get_load_factor()}")
        idx = self.hash_index(key)
        current = self.table[idx]
        if current is None:
            self.table[idx] = HashTableEntry(key, value)
            self.population += 1
            return
        if current.key == key:
            current.value = value
            return
        entry = HashTableEntry(key, value)
        while current.key != key and current.next is not None:
            previous = current
            # find next available spot
            current = current.next
        if current.key == key:
            # re-link with new entry
            previous.next = entry
            previous.next.next = current.next
        else:
            current.next = entry
        self.population += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        result = self.get(key)
        if result is not None:
            self.put(key, None)
        else:
            print(f'NOT FOUND: {key}')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)
        entry = self.table[idx]
        if entry:
            while entry.next and key != entry.key:
                entry = entry.next
            return entry.value
        return entry

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        re = [entry for entry in self.table if entry is not None]  # copy occupied "slots"
        self.capacity = new_capacity  # set new capacity
        self.table = [None] * new_capacity  # create new table
        while len(re) > 0:
            node = re.pop()  # first node
            self.put(node.key, node.value)  # store entry
            while node.next is not None:
                # repeat for every linked node
                node = node.next
                self.put(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
