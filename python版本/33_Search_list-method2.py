class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        l,r = 0, n-1
        while l <= r:
            m = (l+r) // 2
            #print(m)
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                #右边有序
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
