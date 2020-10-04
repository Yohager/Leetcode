class Solution:
    @functools.lru_cache(maxsize=512)
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            return (self.numWays(n-1) + self.numWays(n-2))%1000000007