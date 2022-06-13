class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0 
        i = 0
        n = len(nums)
        while i < n:
            cur = nums[i]
            j = i + 1
            while j < n and nums[j] - cur <= k:
                j += 1
            i = j
            # print(i)
            ans += 1
        return ans 