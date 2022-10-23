class Solution:
    def haveConflict(self, e1: List[str], e2: List[str]) -> bool:
        t = [e1,e2]
        t.sort()
        # print(t)
        f, l = t[0][1], t[1][0]
        f1, f2 = list(map(int,f.split(':')))
        l1, l2 = list(map(int,l.split(':')))
        # print(f1, f2, l1, l2)
        return f1 * 60 + f2 >= l1 * 60 + l2 