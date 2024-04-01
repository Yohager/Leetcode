class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        idx = n - 1
        ret = max(nums)
        while idx >= 1:
            if nums[idx] < nums[idx - 1]:
                idx -= 1
            else:
                temp = nums[idx]
                # print(temp)
                while idx >= 1 and temp >= nums[idx - 1]:
                    temp += nums[idx - 1]
                    idx -= 1
                ret = max(temp, ret)
        return ret
