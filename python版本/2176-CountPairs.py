class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0 
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i < j:
                    if (i*j) % k == 0:
                        # print(i,j)
                        ans += 1
        return ans 