class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ans = []
        i = 0
        n = len(nums)
        while i < n:
            r = i+1
            tmp = nums[i]
            while r < n and nums[r] == tmp + 1:
                tmp = nums[r]
                r += 1
            if i < r-1:
                ans.append(str(nums[i])+"->"+str(nums[r-1]))
            elif i == r-1:
                ans.append(str(nums[i]))
            i = r
        return ans
            
