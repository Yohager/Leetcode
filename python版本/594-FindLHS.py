class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # ans = 0
        # n = len(nums)
        # for i in range(n):
        #     minval = nums[i]
        #     maxval = nums[i]
        #     cnt = 1
        #     j = i 
        #     while j < n:
        #         if maxval - minval != 1:
        #             break 
        #         minval = min(nums[j],minval)
        #         maxval = max(nums[j],maxval)
        #         j += 1
        #         cnt += 1
        #     ans = max(ans,cnt)
        # return ans 
        c = collections.Counter(nums)
        ans = 0 
        for x in c:
            if x+1 in c:
                ans = max(ans,c[x]+c[x+1])
            if x-1 in c:
                ans = max(ans,c[x]+c[x-1])
        return ans 