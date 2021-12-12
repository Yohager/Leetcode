class Solution:
    def countPoints(self, rings: str) -> int:
        d = collections.defaultdict(set)
        n = len(rings)
        for i in range(0,n,2):
            d[rings[i+1]].add(rings[i])
        # print(d)
        ans = 0
        for k in d:
            if 'R' in d[k] and 'G' in d[k] and 'B' in d[k]:
                ans += 1
        return ans 
        