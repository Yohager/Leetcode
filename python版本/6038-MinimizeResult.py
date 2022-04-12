class Solution:
    def minimizeResult(self, e: str) -> str:
        n = len(e)
        arr = e.split('+')
        l1,l2 = len(arr[0]), len(arr[1])
        init = eval(e)
        res = float('inf')
        p1,p2 = -1,-1
        for i in range(l1):
            for j in range(n,n-l2,-1):
                if i == 0 and j == n:
                    cur = e[:i] + '(' + e[i:j] + ')' + e[j:]
                elif i == 0 and j != n:
                    cur = e[:i] + '(' + e[i:j] + ')*' + e[j:]
                elif j == n and i != 0:
                    cur = e[:i] + '*(' + e[i:j] + ')' + e[j:]
                else:
                    cur = e[:i] + '*(' + e[i:j] + ')*' + e[j:]
                # val = eval(cur)
                if eval(cur) < res:
                    p1 = i
                    p2 = j
                    res = eval(cur)
        # print(res,p1,p2)
        if init < res:
            return '(' + e + ')'
        else:
            return e[:p1] + '(' + e[p1:p2] + ')'+e[p2:]