class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        f = {}
        def find(x):
            f.setdefault(x,x)
            while f[x] != x:
                f[x] = f[f[x]]
                x = f[x]
            return x
        
        def union(x,y):
            f[find(x)] = find(y)
        
        tmp = {}
        n = len(accounts)
        for i,j in enumerate(accounts):
            name = j[0]
            emails = j[1:]
            for k in emails:
                if k in tmp:
                    union(i,tmp[k])
                else:
                    tmp[k] = i
        disjoinSet = defaultdict(set)
        for i in range(n):
            temp = find(i)
            for j in accounts[i][1:]:
                disjoinSet[temp].add(j)
        
        ans = []
        for key,val in disjoinSet.items():
            ans.append([accounts[key][0]] + list(sorted(val)))
        
        return ans