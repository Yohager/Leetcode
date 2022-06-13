class Solution:
    def maximumImportance(self, n: int, r: List[List[int]]) -> int:
        deg = [0] * n 
        for x,y in r:
            deg[x] += 1
            deg[y] += 1
        idxs = [i for i in range(n)]
        s = list(zip(deg,idxs))
        s.sort(key=lambda x:(-x[0],x[1]))
        # print(s)
        seq = [e[1] for e in s]
        # print(seq)
        res = 0
        score = [x for x in range(n,0,-1)]
        for v,c in zip(seq,score):
            res += deg[v]*c
        return res 