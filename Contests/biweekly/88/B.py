from sortedcontainers import SortedList 
class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.t = SortedList()

    def upload(self, video: int) -> None:
        self.t.add(video)

    def longest(self) -> int: 
        if not self.t or self.t[0] != 1:
            return 0
        l, r = 0, len(self.t) - 1
        while l <= r:
            m = (l + r) // 2
            if self.t[m] == m + 1:
                # 可以往右边找
                l = m + 1
            else:
                r = m - 1
        # print(l, r)
        return l



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()