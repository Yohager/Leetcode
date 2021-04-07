class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        n = len(height)

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                tmp = stack.pop()
                if not stack:
                    break 
                ans += (min(height[stack[-1]],height[i])-height[tmp]) * (i-stack[-1]-1)
            stack.append(i)
        return ans 