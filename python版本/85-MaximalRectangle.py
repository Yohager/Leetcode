class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        if len(matrix) == 0: return 0
        length = len(matrix)
        width = len(matrix[0])
        heights = [0] * width
        for i in range(length):
            for j in range(width):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            ans = max(ans,self.largestRectangleArea(heights))
        return ans
            


    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        left, right = [0]*len(heights),[0]*len(heights)
        #从左边进行遍历
        monotonic_stack = list()
        for i in range(len(heights)):
            #当栈内有元素时且这个元素大于当前的heights[i]则需要出栈
            while monotonic_stack and heights[monotonic_stack[-1]] >= heights[i]:
                monotonic_stack.pop(-1)
            if monotonic_stack:
                left[i] = monotonic_stack[-1]
            else:
                left[i] = -1
            monotonic_stack.append(i)
            
        #从右边遍历
        monotonic_stack = list()
        for j in range(len(heights)-1,-1,-1):
            while monotonic_stack and heights[monotonic_stack[-1]] >= heights[j]:
                monotonic_stack.pop(-1)
            if monotonic_stack:
                right[j] = monotonic_stack[-1]
            else:
                right[j] = len(heights)
            monotonic_stack.append(j)

        ans = max((right[k] - left[k] - 1)*heights[k] for k in range(len(heights)))
        return ans