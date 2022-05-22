class Solution:
    def minimumLines(self, s: List[List[int]]) -> int:
        s.sort()
        i = 0
        n = len(s)
        if n == 1:
            return 0 
        if n == 2:
            return 1 
        if n == 3:
            return 1 if (s[1][1]-s[0][1] / (s[1][0] - s[0][0])) == (s[2][1]-s[1][1] / (s[2][0] - s[1][0])) else 2 
        ans = 0
        while i < n-1:
            x1,y1 = s[i][0], s[i][1]
            x2,y2 = s[i+1][0], s[i+1][1]
            xl = (y1-y2) / (x1-x2) if x1 != x2 else inf
            j = i + 2
            while j < n:
                x3,y3 = s[j][0], s[j][1]
                xl2 = (y2-y3) / (x2-x3) if x2 != x3 else inf 
                if xl2 != xl:
                    break 
                x2,y2 = x3, y3 
                j += 1
            i = j - 1
            # print(i)
            ans += 1
        return ans 
                
                
                