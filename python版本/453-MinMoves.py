class Solution(object):
    def minMoves(self, nums):
        sum = 0
        minmum = min(nums)
        for i in nums:
            sum += i-minmum
        return sum