class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = []


    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)
    def remove(self, key: int) -> None:
        for idx,val in enumerate(self.hashset):
            if key == val:
                self.hashset.pop(idx)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return True if key in self.hashset else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)