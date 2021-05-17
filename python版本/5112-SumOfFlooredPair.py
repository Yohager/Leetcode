class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()

        def binarysearch(i,j):
            return bisect.bisect_left(nums,nums[i]*j)
        
        ans = 0
        for i in range(len(nums)):
            j = 1
            while nums[i]*j <= nums[-1]:
                x = binarysearch(i,j)
                ans += len(nums) - x 
                j += 1
        return ans % MOD