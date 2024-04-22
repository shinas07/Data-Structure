# This use linked lists to store key-value pairs.
class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_value = self._hash(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = Node(key, value)
        else:
            current = self.table[hash_value]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        hash_value = self._hash(key)
        current = self.table[hash_value]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self, key):
        hash_value = self._hash(key)
        current = self.table[hash_value]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[hash_value] = current.next
                return
            prev = current
            current = current.next


ht = HashTable(10)
ht.insert("name","Shinas")
ht.insert("age",77)
ht.insert("city","Calicut")

print(ht.get('name'))
print(ht.get('age'))
print(ht.get('city'))

ht.delete('name')
print(ht.get('name'))
