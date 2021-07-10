class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tmp = [j[-1] for j in orders]
        tmp = list(set(tmp))
        tmp.sort()
        idxs = ["Table"] + list(tmp)
        res = []
        res.append(idxs)
        d = collections.defaultdict(list)
        for i in orders:
            d[i[1]].append(i[2])
        tables = sorted(d.keys(),key=lambda x:int(x))
        for x in tables:
            cur = []
            cur.append(x)
            c = collections.Counter(d[x])
            for k in idxs[1:]:
                if k in c.keys():
                    cur.append(str(c[k]))
                else:
                    cur.append('0')
            res.append(cur)
        return res 
