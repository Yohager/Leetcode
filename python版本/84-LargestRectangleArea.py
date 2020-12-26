class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        暴力法时间复杂度为O(N^2)不可取
        这里使用到的技巧是单调栈
        '''
        # ans = 0
        # for i in range(len(heights)):
        #     height = heights[i]
        #     j = i - 1
        #     length = 1
        #     while j >= 0 and heights[j] >= height:
        #         length += 1
        #         j -= 1
        #     j = i + 1
        #     while j < len(heights) and heights[j] >= height:
        #         length += 1
        #         j += 1
            
        #     ans = max(ans,height*length)
        # return ans
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
        
