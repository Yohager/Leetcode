class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        n = len(nums)
        l,r = 0,0
        while r < n:
            if nums[l] == nums[r]:
                r += 1
            else:
                nums[l+1] = nums[r]
                r += 1
                l += 1
        return l+1