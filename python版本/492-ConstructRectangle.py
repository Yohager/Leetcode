class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math 
        num = int(math.sqrt(area))
        ans = []
        for n in range(num,-1,-1):
            if area % n == 0:
                ans.append(n)
                break 
        ans.append(area//n)
        ans.sort(reverse=True)
        return ans 