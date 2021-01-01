class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        i = 1
        index = 0
        while i <= n:
            if index < len(nums) and nums[index] <= i:
                i += nums[index]
                index += 1
                #length += i
            else:
                ans += 1
                #length += i
                i += i
        return ans
            


        
