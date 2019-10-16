class Solution:
    def maxSubArray(self, nums) -> int:
        sum_num = sum(nums)
        i = 0
        while i<len(nums):
            