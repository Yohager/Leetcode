class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        stack = []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i % n]:
                ans[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return ans 

