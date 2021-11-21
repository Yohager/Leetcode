class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # c = collections.Counter(colors)
        n = len(colors)
        # cols = c.keys()
        # ans = 0
        # for col in cols:
        ans = 0
        idx = 0 
        while idx < n:
            tmp = colors[idx]
            for j in range(n-1,-1,-1):
                if colors[j] != tmp:
                    ans = max(ans,j-idx)
            idx += 1
        return ans 