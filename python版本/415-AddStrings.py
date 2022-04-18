class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n1,n2 = len(num1), len(num2)
        i,j = n1-1,n2-1
        extra = 0
        ans = ''
        while i >= 0 or j >= 0:
            tmp = 0
            if i >= 0 and j >= 0:
                c1,c2 = d[num1[i]],d[num2[j]]
                tmp = c1 + c2 + extra 
            elif i >= 0 and j < 0:
                tmp = d[num1[i]] + extra 
            else:
                tmp = d[num2[j]] + extra 
            extra = tmp // 10
            v = tmp % 10 
            ans += str(v)
            i -= 1
            j -= 1
        if extra != 0:
            ans += str(extra)
        return ''.join(list(ans)[::-1])