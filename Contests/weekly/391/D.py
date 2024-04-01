class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        from sortedcontainers import SortedList
        s1 = SortedList()
        s2 = SortedList()
        
        for x, y in points:
            s1.add(x + y)
            s2.add(x - y)
        
        ans = inf 
        
        # 枚举要删除的点
        for x, y in points:
            s1.remove(x + y)
            s2.remove(x - y)
            
            # print(s1, s2)
            
            ans = min(ans, max(s1[-1] - s1[0], s2[-1] - s2[0]))
            
            s1.add(x + y)
            s2.add(x - y)
        return ans 
