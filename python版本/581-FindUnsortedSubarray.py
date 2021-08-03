class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        if temp == nums:
            return 0
        l,r = 0,0
        n = len(nums)
        for i in range(n):
            if nums[i] != temp[i]:
                l = i 
                break 
        for j in range(n-1,-1,-1):
            if nums[j] != temp[j]:
                r = j 
                break 
        #print(l,r)
        return r-l+1
            