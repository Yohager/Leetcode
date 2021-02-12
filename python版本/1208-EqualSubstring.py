class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        dist = []
        for i in range(n):
            dist.append(abs(ord(s[i])-ord(t[i])))
        #print(dist)
        ans = 0
        l,r = 0,0
        cost = 0
        while r < n:
            cost += dist[r]
            while cost > maxCost:
                ans = max(ans,r-l)
                cost -= dist[l]
                l += 1
            r += 1
        ans = max(ans,r-l)
        return ans