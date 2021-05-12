class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums:
            return ans 
        nums.sort()
        n = len(nums)
        visited = [0] * n 
        def backtrack(arr,length):
            if length == n:
                ans.append(arr)
            for i in range(n):
                if visited[i] or (i>0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = 1
                backtrack(arr+[nums[i]],length+1)
                visited[i] = 0
        
        def func1(nums,arr,length):
            if length == n and arr not in ans:
                ans.append(arr)
            for i in range(len(nums)):
                func1(nums[:i]+nums[i+1:],arr+[nums[i]],length+1)
        
        backtrack([],0)
        return ans