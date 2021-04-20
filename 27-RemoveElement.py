class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l,r = 0,0
        while r < n:
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l


