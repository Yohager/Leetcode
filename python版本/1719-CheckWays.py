class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        ans = 1 
        c1 = defaultdict(int)
        c2 = defaultdict(set)
        for x,y in pairs:
            c1[x] += 1
            c1[y] += 1
            c2[x].add(y)
            c2[y].add(x)
        
        for x,y in pairs:
            if c1[x] == c1[y]: 
                ans = 2

        nodes = list(c1.keys())
        nodes.sort(key=lambda x:-c1[x])
        num = len(nodes)
        # print(nodes)
        root = nodes[0]
        if c1[root] != num - 1:
            ans = 0
        else:
            ancestors = dict()
            for node in nodes:
                ancestors[node] = root
            flag = True 
            vis = set()
            vis.add(root)
            for x in nodes[1:]:
                for y in c2[x]:
                    if y not in vis:
                        if ancestors[y] != ancestors[x]:
                            ans = 0
                            flag = False 
                            break 
                    ancestors[y] = x 
                if not flag:
                    break 
                vis.add(x)
        return ans 


