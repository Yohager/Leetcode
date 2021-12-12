class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        import math
        def dist(x1,y1,x2,y2):
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        d = collections.defaultdict(set)
        n = len(bombs)
        for i in range(n):
            for j in range(i+1,n):
                tmp = dist(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1])
                if tmp <= bombs[i][2]:
                    d[i].add(j)
                if tmp <= bombs[j][2]:
                    d[j].add(i)
        #print(d)
        # 构建directed graph 
        if not d.keys():
            return 1
        ans = 0
        arrs = list(d.keys())
        for i in arrs:
            tmp = 0 
            q = deque()
            q.append(i)
            vis = [False] * n
            #print('here cur i:',i)
            while q:
                cur = q.popleft()
                vis[cur] = True
                tmp += 1
                for x in d[cur]:
                    if not vis[x] and x not in q:
                        q.append(x)
                #print(q)
            #print(tmp)
            ans = max(ans, tmp)
        return ans 
                
            