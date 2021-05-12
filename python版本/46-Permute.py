class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums:
            return ans
        def backtrack(arr,tmp):
            if not arr:
                ans.append(tmp)
                return 
            for i in range(len(arr)):
                backtrack(arr[:i]+arr[i+1:],tmp + [arr[i]])
        backtrack(nums,[])
        return ans 