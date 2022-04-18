class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)
        if n1 > n2:
            return False 
        
        l,r = 0,0 
        d1 = {}
        d2 = {}
        for x in s1:
            d1[x] = d1.get(x,0) + 1
        
        while l < n2 and r < n2:
            while r - l < n1:
                d2[s2[r]] = d2.get(s2[r],0) + 1
                r += 1
            
            if r - l == n1:
                if d1 == d2:
                    return True 
                cur = s2[l]
                d2[cur] -= 1 
                if d2[cur] == 0:
                    d2.pop(cur)
                l += 1
        return False