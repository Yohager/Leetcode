class Solution:
    # @lru_cache(None)
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # if len(nums) == 2:
        #     return nums[0] + nums[1]
        tmp = []
        for i in range(len(nums)-1):
            # if nums[i] + nums[i+1] < 10:
            #     tmp.append(nums[i]+nums[i+1])
            # else:
            tmp.append((nums[i]+nums[i+1])%10)
        return self.triangularSum(tmp)