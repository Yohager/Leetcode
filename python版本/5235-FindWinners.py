class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        c = Counter()
        n = set()
        for x,y in matches:
            c[y] += 1
            n.add(x)
            n.add(y)
        # c表示每个玩家输了多少场
        a1 = []
        a2 = []
        for p in n:
            if c[p] == 0:
                a1.append(p)
            elif c[p] == 1:
                a2.append(p)
        a1.sort()
        a2.sort()
        return [a1,a2]