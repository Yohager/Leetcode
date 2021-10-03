class Solution:
    def numOfPairs(self, nums: List[str], t: str) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(n):
                if nums[i] + nums[j] == t and i != j:
                    ans += 1
        return ans 