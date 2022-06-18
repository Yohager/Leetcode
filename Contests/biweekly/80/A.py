class Solution:
    def strongPasswordCheckerII(self, p: str) -> bool:
        if len(p) < 8:
            return False 
        c1,c2,c3,c4 = 0,0,0,0
        for x in p:
            if x.isdigit():
                c1 += 1
            elif x.isalpha():
                if x.isupper():
                    c2 += 1
                else:
                    c3 += 1
            elif x in "!@#$%^&*()-+":
                c4 += 1
        if c1 == 0 or c2 == 0 or c3 == 0 or c4 == 0:
            return False 
        n = len(p)
        for i in range(n-1):
            if p[i] == p[i+1]:
                return False 
        return True 
                    