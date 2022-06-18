class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n+1) 
        for i in range(n):
            p[i+1] = p[i] + nums[i]
        # print(p)
        i,j = 1,1
        ans = 0
        while j <= n:
            while i <= j and (p[j] - p[i-1]) * (j-i+1) >= k:
                i += 1
            ans += (j-i+1)
            j += 1
        return ans 