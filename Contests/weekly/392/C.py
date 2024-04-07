class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        m = (n - 1) // 2 if n % 2 == 1 else n // 2
        if nums[m] == k:
            return ans
        idx = bisect.bisect_right(nums, k)
        # 区间内的数全部需要进行变更
        if idx == m:
            minv = m 
            maxv = m + 1
        elif idx < m:
            minv = idx 
            maxv = m + 1
        else:
            minv = m 
            maxv = idx
        # print(minv, maxv)
        for j in range(minv, maxv):
            # print(abs(nums[j] - k))
            ans += abs(nums[j] - k)
        return ans 
            
        
        
