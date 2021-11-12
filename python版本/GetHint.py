class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b,c = 0,0
        ns,ng = '',''
        for x,y in zip(secret,guess):
            if x == y: b += 1
            else:
                ns += x
                ng += y 
        
        c1 = collections.Counter(ns)
        c2 = collections.Counter(ng)
        for k in c1:
            if k in c2:
                if c1[k] >= c2[k]:
                    c += c2[k]
                else:
                    c += c1[k]
        return str(b) + 'A' + str(c) + 'B'