class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counters = collections.Counter()
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                tmp = nums[i]*nums[j]
                ans += 8*counters[tmp]
                counters[tmp] += 1
        return ans