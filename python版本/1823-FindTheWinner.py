class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        l = list(range(1,n+1))
        idx = 0
        while l:
            tmp = l.pop(0)
            idx += 1
            if idx == k:
                idx = 0
                continue
            l.append(tmp)
            if len(l) == 1:
                break
        return l[0]