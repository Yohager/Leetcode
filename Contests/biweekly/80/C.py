class Solution:
    def matchReplacement(self, s: str, sub: str, m: List[List[str]]) -> bool:
        n = len(s)
        t = len(sub)
        d = defaultdict(set)
        for x,y in m:
            d[x].add(y)
        def check(p,q):
            for i in range(t):
                if q[i] != p[i]:
                    if p[i] not in d[q[i]]:
                        return False 
            return True 
        
        for i in range(0,n-t+1):
            if check(s[i:i+t],sub):
                return True 
        return False 