class Solution:
    def asteroidsDestroyed(self, m: int, a: List[int]) -> bool:
        a.sort()
        n = len(a)
        tmp = m
        for i in range(n):
            if tmp < a[i]:
                return False 
            tmp += a[i]
        return True
        