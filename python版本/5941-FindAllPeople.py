class Solution:
    def findAllPeople(self, n: int, m: List[List[int]], f: int) -> List[int]:
        d = collections.defaultdict(list)
        # print(ms)
        for x,y,z in m:
            d[z].append([x,y])
        d[0].append([0,f])
        times = sorted(d.keys())
        ans = set([0])
        for t in times:
            tmp = set()
            d2 = collections.defaultdict(set)
            for x,y in d[t]:
                d2[x].add(y)
                d2[y].add(x)
                if x in ans:
                    tmp.add(x)
                if y in ans:
                    tmp.add(y)
            q = list(tmp)
            while q:
                cur = q.pop()
                for nex in d2[cur]:
                    if nex in tmp:
                        continue 
                    tmp.add(nex)
                    q.append(nex)
                    ans.add(nex)
        return list(ans)