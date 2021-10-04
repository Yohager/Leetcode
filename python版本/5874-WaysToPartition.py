class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        
        d1 = {}
        d2 = {}
        for i in range(1,len(nums)):
            d1[2*pre[i]-pre[-1]] = d1.get(2*pre[i]-pre[-1],0) + 1
        ans= max(ans,d1.get(0,0))
        for i in range(n):
            diff = k - nums[i]
            ans = max(ans,d1.get(-diff,0)+d2.get(diff,0))
            tmp = 2*pre[i+1] - pre[-1]
            if i == n-1:
                continue 
            d1[tmp] -= 1
            d2[tmp] = d2.get(tmp,0) + 1
        return ans 