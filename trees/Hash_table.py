class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_func(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_func(key)

        if not self.table[index]:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            temp = self.table[index]

            while temp:
                if temp.key == key:
                    temp.value = value
                    return
                temp = temp.next

            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def delete(self, key):
        index = self.hash_func(key)

        temp = self.table[index]
        prev = None

        while temp:
            if temp.key == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.table[index] = temp.next

                self.size -= 1
                return
            prev = temp
            temp = temp.next

        raise KeyError(key)

    def table_size(self):
        return self.size

    def find(self, key):
        index = self.hash_func(key)
        temp = self.table[index]

        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next

        raise KeyError(key)


# Test :
hash_table = HashTable()

# Insert :
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("orange", 3)


apple_value = hash_table.find("apple")
print(apple_value)  # Output: 5


hash_table.delete("banana")


table_size = hash_table.table_size()
print(table_size)  # Output: 2
