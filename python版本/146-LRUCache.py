class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.c = capacity
        self.cur_l = 0


    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value 
            self.d.move_to_end(key)
            return 
        if self.cur_l < self.c:
            # 没有超过容量直接添加
            self.d[key] = value 
            self.cur_l += 1
        else: 
            self.d.popitem(0)
            self.d[key] = value 
        # print(self.d)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)