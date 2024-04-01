class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # 枚举右端点
        ans = 0
        record = 0
        for i, val in enumerate(nums):
            if i >= 1 and val == nums[i - 1]:
                record = 1
            else:
                record += 1
            ans += record
        return ans
            
