class Solution:
    def longestObstacleCourseAtEachPosition(self, O: List[int]) -> List[int]:
        ans = []
        stk = []
        for o in O:
            if not stk or stk[-1] <= o:
                stk.append(o)
                ans.append(len(stk))
            else:
                idx = bisect.bisect_right(stk,o)
                stk[idx] = o 
                ans.append(idx+1)
        return ans 