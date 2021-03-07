edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
graph = [[] for _ in range(6)]
for u,v,w in edges:
    graph[u].append((v,w))
    graph[v].append((u,w))

print(graph)

dist = [float('inf'),4,2,1,6,0]
d = list(range(6))
d = sorted(d,key=lambda x: dist[x])

dp = [0 for _ in range(6)]

dp[5] = 1

print('sort:',d)
for u in d:
    print('node:',u)
    print('grpah:',graph[u])
    for v,w in graph[u]:
        if dist[u] > dist[v]:
            dp[u] += dp[v]
    print(dp[u])

print(dp)

