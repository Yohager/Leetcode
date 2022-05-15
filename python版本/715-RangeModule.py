import bisect 

class RangeContainers():
    def __init__(self):
        self.range = []
        self.cnt = 0
    
    def addRange(self,left,right):
        l = bisect.bisect_left(self.range,left,key=lambda x:x[1])
        r = bisect.bisect_right(self.range,right,key=lambda x:x[0])
        if l < r:
            left = min(left,self.range[l][0])
            right = max(right,self.range[r-1][1])
            # 将lr区间的值去掉
            for i in range(l,r):
                self.cnt -= self.range[i][1] - self.range[i][0]
            self.range = self.range[:l] + [[left,right]] + self.range[r:]
        
        else:
            self.range.insert(l,[left,right])
        self.cnt += right - left 
    
    def queryRange(self,left,right):
        idx = bisect.bisect_right(self.range,left,key=lambda x:x[0]) - 1
        return 0 <= idx < len(self.range) and self.range[idx][1] >= right 

    def removeRange(self,left,right):
        l = bisect.bisect_right(self.range,left,key=lambda x:x[1])
        r = bisect.bisect_left(self.range,right,key=lambda x:x[0])

        if l < r:
            R = []
            if self.range[l][0] < left:
                R.append([self.range[l][0],left])
            if self.range[r-1][1] > right:
                R.append([right,self.range[r-1][1]])
            for i in range(l,r):
                self.cnt -= self.range[i][1] - self.range[i][0]
            self.range = self.range[:l] + R + self.range[r:]
            for rl,rr in  R:
                self.cnt += rr-rl 
    
    def count(self):
        return self.cnt 


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

class RangeModule:

    def __init__(self):
        self.c = RangeContainers()


    def addRange(self, left: int, right: int) -> None:
        self.c.addRange(left,right)


    def queryRange(self, left: int, right: int) -> bool:
        return self.c.queryRange(left,right)

    def removeRange(self, left: int, right: int) -> None:
        self.c.removeRange(left,right)



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)