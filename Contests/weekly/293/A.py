class Solution:
    def removeAnagrams(self, w: List[str]) -> List[str]:
        n = len(w)
        vis = [True] * n 
        idx = 0
        while idx < n:
            cur = w[idx]
            while idx+1 < n and Counter(w[idx+1]) == Counter(cur):
                vis[idx+1] = False 
                idx += 1
            idx += 1
        ans = []
        for i in range(n):
            if vis[i]:
                ans.append(w[i])
        return ans 