class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        acc = list(accumulate(nums, initial=0))
        # print(acc)
        ans = []
        for q in queries:
            idx = bisect.bisect_left(nums, q)
            # print(idx)
            increase = idx * q - acc[idx]
            decrease = acc[-1] - acc[idx] - (n - idx) * q
            ans.append(increase + decrease)
        return ans 
            

