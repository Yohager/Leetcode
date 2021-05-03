class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        minval = float('inf')
        for i in range(n):
            if nums[i] == target:
                minval = min(minval,abs(i-start))
        return minval