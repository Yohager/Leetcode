class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        times = n // 3 
        ans = []
        c = collections.Counter(nums)
        for x in c:
            if c[x] > times:
                ans.append(x)
        return ans