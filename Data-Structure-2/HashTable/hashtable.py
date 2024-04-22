class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        for i, (exist_key, exist_value) in enumerate(bucket):
            if exist_key == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))

    def get(self,key):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        for exist_key, exist_value in bucket:
            if exist_key == key:
                return exist_value
        return KeyError("Key Not Found")
    
    def delete(self, key):
        hash_vlaue = self._hash(key)
        bucket = self.table[hash_vlaue]

        for i, (exist_key, exist_value) in enumerate(bucket):
            if exist_key == key:
                del bucket[i]
                return
        raise KeyError("Key Not Found")

ht = HashTable(6)
ht.insert("apple",10)
ht.insert("banana",4)
ht.insert("orange",8)
print(ht.get("apple"))
