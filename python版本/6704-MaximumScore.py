class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = k,k
        ans = 0
        while True:
            while r < n and nums[r] >= nums[k]:
                r += 1
            while l >= 0 and nums[l] >= nums[k]:
                l -= 1
            ans = max(ans,(r-l-1)*nums[k])
            if l < 0 and r == n:
                break 
            if l >= 0 and r < n:
                nums[k] = max(nums[l],nums[r])
            elif l < 0:
                nums[k] = nums[r]
            else:
                nums[k] = nums[l]
        return ans 
