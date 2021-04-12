class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        l,r = 0,n-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True
            if nums[l] == nums[r]:
                l += 1
                continue
            if nums[m] <= nums[r]:
                #此时右半边的数组是有序的
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return False