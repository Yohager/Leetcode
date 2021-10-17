class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def func(arr):
            tmp = arr[0]
            for a in arr[1:]:
                tmp = tmp | a 
            return tmp 
        
        def get_sub_sets(arr):
            subsets = [[]]
            for a in arr:
                subsets.extend([item + [a] for item in subsets])
            return subsets
        
        maxval = func(nums)
        subsets = get_sub_sets(nums)
        ans = 0
        for subset in subsets:
            if not subset:
                continue 
            if func(subset) == maxval:
                ans += 1
        return ans 