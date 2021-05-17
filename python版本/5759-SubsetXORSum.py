class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from itertools import combinations
        def subsets(arr):
            ans = []
            for i in range(0,len(arr)+1):
                temp = [list(x) for x in combinations(arr,i)]
                if len(temp) > 0:
                    ans.extend(temp)
            return ans 
        subs = subsets(nums)
        ans = 0
        for i in subs:
            k = 0
            for j in i:
                k ^= j
            ans += k
        return ans