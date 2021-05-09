class Solution:
    def maxSumMinProduct(self, heights: List[int]) -> int:
        sum1 = [0] * (len(heights)+1)
        for elem in range(1,len(heights)+1):
            sum1[elem] += sum1[elem-1] + heights[elem-1]
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
        #print(left,right)
        ans = 0
        for x in range(len(heights)):
            tmp = (sum1[right[x]]-sum1[left[x]+1]) * heights[x]
            #print(tmp)
            ans = max(ans,tmp)
        return int(ans % 1000000007)