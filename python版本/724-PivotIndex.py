class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1
        n = len(nums)
        total = sum(nums)
        ls = 0
        for i in range(n):
            if 2 * ls == total - nums[i]:
                return i 
            ls += nums[i]
        return -1
