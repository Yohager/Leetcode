from sortedcontainers import SortedSet
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int) 
        players = SortedSet()
        for x, y in matches:
            players.add(x)
            players.add(y)
            d[y] += 1
        ans = [[], []]
        for p in players:
            if d[p] == 0:
                ans[0].append(p)
            elif d[p] == 1:
                ans[1].append(p)
        return ans
 
