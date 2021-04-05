class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict
        n = len(logs)
        d = defaultdict(set)
        for t in logs:
            d[t[0]].add(t[1])
        print(d)
        ans = []
        for s in d:
            ans.append(len(d[s]))
        c = collections.Counter(ans)
        res = [0 for _ in range(k)]
        #print(res)
        print(c)
        for i in range(k):
            if i+1 in c:
                res[i] = c[i+1]
        return res