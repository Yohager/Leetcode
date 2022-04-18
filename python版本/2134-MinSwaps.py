class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums) # total表示了nums中一共有多少个1
        if n == total: return 0 
        # 第一种情况
        # 左边为0，中间为1，右边为0
        # 求前缀和，找大小为total的区间其中区间的和最大的值
        prefix = []
        cur = 0
        for i in range(n):
            cur += nums[i]
            prefix.append(cur)
        # 找prefix的相隔total大小的区间
        v = -float('inf')
        for i in range(n-total):
            v = max(v,prefix[total+i]-prefix[i])
        ans1 = total - v # 这里计算的是第一种情况
        
        # 第二种情况
        # 左边为1，中间为0，右边为1
        size = n-total 
        v2 = float('inf')
        for j in range(total):
            v2 = min(v2,prefix[n-total+j]-prefix[j])
        ans2 = v2 
        return min(ans1,ans2)