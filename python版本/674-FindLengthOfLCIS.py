class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        n = len(nums)
        ans = 1
        begin = 0
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                tmp = i - begin + 1
                if tmp > ans:
                    ans = tmp
                begin = i+1
        tmp= n - begin
        if tmp > ans:
            ans = tmp
        return ans
