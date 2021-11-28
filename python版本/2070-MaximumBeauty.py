class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maxvals = [(0,0)]
        # maxvals = []
        cur_m = 0
        for p,b in items:
            cur_m = max(cur_m,b)
            maxvals.append((p,cur_m))
        
        #print(maxvals)
        ans = []
        for q in queries:
            idx = bisect.bisect_left(maxvals,(q,10000000000)) - 1
            ans.append(maxvals[idx][1])
        return ans 