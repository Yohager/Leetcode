class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + dfs(num // 2)
            else:
                return 1 + min(dfs(num+1), dfs(num-1))
        return dfs(n)