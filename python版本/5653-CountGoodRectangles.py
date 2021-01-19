class Solution:
    def countGoodRectangles(self, r: List[List[int]]) -> int:
        ans = []
        for i,j in r:
            if i <= j:
                ans.append(i)
            else:
                ans.append(j)
        
        maxlen = max(ans)
        counts = 0
        for i in ans:
            if i == maxlen:
                counts += 1
        return counts