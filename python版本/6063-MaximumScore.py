class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x,y in edges:
            bisect.insort(g[x],[-scores[y],y])
            bisect.insort(g[y],[-scores[x],x])
        # print(g)

        ans = -1
        for x,y in edges:
            # 当前边作为中间的边，向两侧扩展
            left = g[x][:min(len(g[x]),3)]
            right = g[y][:min(len(g[y]),3)]
            for l in left:
                for r in right:
                    if l[1] != y and l[1] != r[1] and r[1] != x:
                        # print(x,y,l[1],r[1])
                        ans = max(ans, scores[x] + scores[y] - l[0] - r[0])
        return ans 
