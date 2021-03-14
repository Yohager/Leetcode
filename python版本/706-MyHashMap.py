class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = []


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if not self.hashmap:
            self.hashmap.append([key,value])
        flag = 0
        for i in self.hashmap:
            if i[0] == key:
                i[1] = value
                flag = 1
                break 
        if flag == 0:
            self.hashmap.append([key,value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if not self.hashmap:
            return -1
        else:
            for i in self.hashmap:
                if i[0] == key:
                    return i[1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in self.hashmap:
            if i[0] == key:
                self.hashmap.remove(i)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)