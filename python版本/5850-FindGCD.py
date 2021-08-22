class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        minval,maxval = nums[0],nums[-1]
        ans = 1
        for i in range(1,minval+1):
            if minval % i == 0 and maxval % i == 0:
                ans = max(ans,i)
        return ans 