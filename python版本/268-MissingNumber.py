class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(range(n+1)) - sum(nums)