class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m 
        self.k = k
        self.nums = []
        self.counts = 0
        self.container = []


    def addElement(self, num: int) -> None:
        # import bisect
        # bisect.insort(self.nums,num)
        self.nums.append(num)
        self.counts += 1


    def calculateMKAverage(self) -> int:
        if self.counts < self.m:
            return -1
        else:
            tmp = self.nums[-self.m:]
            tmp.sort()
            return int(sum(tmp[self.k:-self.k])/len(tmp[self.k:-self.k]))
            



# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()