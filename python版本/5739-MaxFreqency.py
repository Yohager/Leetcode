class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        '''
        使用双指针求解
        用双指针维护一个滑窗
        滑窗里面是在这个范围内维护的最多的频数
        频数用ans记录，不断更新
        '''
        l,r = 0,0
        ans = 0
        tmp = 0
        q = nums[0]
        while r < n:
            #右指针不断向右移动，左指针根据情况调整
            tmp += (r-l) * (nums[r]-q)
            while tmp > k:
                tmp -= nums[r] - nums[l]
                l += 1
            ans = max(ans,r-l+1)
            q = nums[r]
            r += 1
        return ans