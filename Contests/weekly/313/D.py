class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i):
            if i >= n:
                return 0 
            ans = 1
            for j in range(i + 1, i + (n - i) // 2 + 1):
                if s[i:j] == s[j:j+j-i]:
                    ans = max(ans, 1 + dfs(j))
            return ans 
        return dfs(0)