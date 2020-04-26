from builtins import object


class MyHashDictionary(object):

    def __init__(self):
        """
        Initialize the data structure required for hash table
        """
        self.hash_table = [None] * 8
        self.hash_table_capacity = 8
        self.size = 0
        self.threshold_load_factor = float(2) / 3

    def hash_function(self, key):
        if isinstance(key, int):
            return key % self.hash_table_capacity
        else:
            pass

    def hash_function_2(self, key):
        if isinstance(key, int):
            return key % self.hash_table_capacity
        else:
            pass

    def insert(self, key, value):
        # double the table if load factor becomes less than
        # or equal to threshold load factor
        load_factor = self.size / self.hash_table_capacity
        if load_factor <= self.threshold_load_factor:
            current_htable = self.hash_table

            self.hash_table = [None] * (self.hash_table_capacity * 2)
            for i in range(current_htable):
                if current_htable[i] != None or current_htable[i] == "==DeletedSlotReadyToOccupy@@":
                    continue
                else:
                    hash_value = self.hash_function(i)
