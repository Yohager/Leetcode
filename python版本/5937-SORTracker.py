class SORTracker:

    def __init__(self):
        self.get_cnt = 0
        self.arr = []


    def add(self, name: str, score: int) -> None:
        if not self.arr:
            self.arr.append([-score,name])
        else:
            #idx = bisect.bisect_left(self.arr,[score,name])
            bisect.insort_right(self.arr,[-score,name])

    def get(self) -> str:
        #print(self.arr)
        ans = self.arr[self.get_cnt][1]
        self.get_cnt += 1
        return ans 
    
# [null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]
# [null ,null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()