class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        for i, x in enumerate(nums):
            r = i + 1
            cur = x
            temp = 1
            while r < n:
                if nums[r] <= cur:
                    break
                else:
                    temp += 1
                    cur = nums[r]
                r += 1
            # print(temp)
            ans = max(ans, temp)
        for i, x in enumerate(nums):
            r = i + 1
            cur = x 
            temp2 = 1
            while r < n:
                if nums[r] >= cur:
                    break
                else:
                    temp2 += 1
                    cur = nums[r]
                r += 1
            ans = max(ans, temp2)
        return ans 
            
                
                
        
                
        

