class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -float('inf') # 定义需要维护的值
        l,r = 0,0
        n = len(nums)
        total = 0 # 定义需要维护的值
        while l < n and r < n:
            while r-l < k: # 当前窗口还没有达到需要的大小
                total += nums[r]
                r += 1
            if r-l == k: # 当前窗口达到了要求的大小
                ans = max(ans,total/k)
                total -= nums[l] # 移动左指针前更新需要维护的变量的大小
                l += 1
        return ans 