class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = [[gt,idx] for idx,gt in enumerate(growTime)]
        arr.sort(key=lambda x:[-x[0],x[1]])
        ans = 0
        day = 0
        for x,i in arr:
            day += plantTime[i]
            ans = max(ans,day+x)
        return ans 