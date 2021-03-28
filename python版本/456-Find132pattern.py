class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        tmp = nums[0]
        n = len(nums)
        for i in range(1,n):
            for j in range(n-1,i,-1):
                if tmp < nums[j] and nums[j] < nums[i]:
                    return True
            tmp = min(tmp,nums[i])
        return False