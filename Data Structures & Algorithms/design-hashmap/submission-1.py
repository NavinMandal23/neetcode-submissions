class MyHashMap:

    def __init__(self):
        self.hm = []

    def put(self, key: int, value: int) -> None:
        for kv in self.hm:
            if kv[0] == key:
                kv[1] = value
                return
        self.hm.append([key, value])

    def get(self, key: int) -> int:
        for kv in self.hm:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.hm):
            if kv[0] == key:
                self.hm.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)