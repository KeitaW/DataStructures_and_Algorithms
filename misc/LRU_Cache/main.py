# https://www.kunxi.org/2014/05/lru-cache-in-python/
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = 0
        self.cache = {}
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru[key] = self.counter
            self.counter += 1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            # This is O(N) hence not efficient.
            oldest_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            print("oldestkey", oldest_key)
            self.cache.pop(oldest_key)
            self.lru.pop(oldest_key)
        self.cache[key] = value
        self.lru[key] = self.counter
        self.counter += 1
