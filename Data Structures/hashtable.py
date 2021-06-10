class HashTable:
    def __init__(self):
        self.size = 10
        self.hash_map = [[] for _ in range(self.size)]
        # print(self.hash_map)

    def _hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hashed_key = self._hashing_func(key)
        key_exists = False
        slot = self.hash_map[hashed_key]

        for i, kv in enumerate(slot):
            k, v = kv
            if k == key:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hashed_key = self._hashing_func(key)
        slot = self.hash_map[hashed_key]

        for i, kv in enumerate(slot):
            k, v = kv
            if k == key:
                return v
        raise KeyError('does not exist.')

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


d = HashTable()

d.set(10, 'b')
d.set(20, 'a')
d['nazli'] = 'n'

print(d['nazli'])
