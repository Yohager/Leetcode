class Solution:
    def memLeak(self, m1: int, m2: int) -> List[int]:
        MAXSIZE = 2 ** 32 - 1
        cur = max(m1,m2)
        flag = 0
        ans = 0
        if cur == m1:
            flag = 0
        else:
            flag = 1
        for i in range(1,MAXSIZE):
            cur -= i
            if cur < 0:
                ans = i
                break
            if flag == 0:
                m1 -= i
            else:
                m2 -= i
            cur = max(m1,m2)
            if cur == m1:
                flag = 0
            else:
                flag = 1
            
        return [ans,m1,m2]