class Solution:
    def convertTime(self, a: str, b: str) -> int:
        if a == b:
            return 0
        def cals(t1,t2):
            res = 0
            diff = t2[1] - t1[1]
            while diff:
                if diff >= 15:
                    diff -= 15 
                    res += 1
                elif 5 <= diff < 15:
                    diff -= 5
                    res += 1
                elif diff < 5:
                    diff -= 1
                    res += 1
            res += (t2[0]-t1[0])
            return res 
        t1 = list(map(int,a.split(':')))
        t2 = list(map(int,b.split(':')))
        if t2[1] < t1[1]:
            t2[1] += 60 
            t2[0] -= 1
        return cals(t1,t2)
            