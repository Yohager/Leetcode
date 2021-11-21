class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = collections.defaultdict(list)
        n = len(arr)
        for i in range(n):
            self.d[arr[i]].append(i)


    def query(self, left: int, right: int, value: int) -> int:
        tmp = self.d[value]
        l = bisect.bisect(tmp,left-1)
        r = bisect.bisect(tmp,right)
        return r-l
        



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)