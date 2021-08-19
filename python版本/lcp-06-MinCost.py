class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0 
        for x in coins:
            ans += (x+1) // 2
        return ans 