'''
考虑需要判断当前的图中是否有环的问题
使用拓扑排序
1. 无向图: 
(1) 计算所有节点的度
(2) 将所有度<=1的节点入队
(3) 当队列不为空的时候弹出队首元素并将其相邻元素节点的度全部-1, 减完后若度为1则节点入队
(4) 循环结束之后判断已经访问的节点的数量是否等于n
2. 有向图
将(2)中所有度<=1的节点入队改为将所有度为0的节点入队

考虑使用dfs
基本思路 深度优先遍历图如果在遍历的过程中发现存在节点有一条边指向已经访问到的节点
并且这个已经访问过的节点不是上一步访问的节点则表示有环
'''
from collections import defaultdict,deque


def TopologicalSorting(n,edges):
    d1 = defaultdict(set)
    d2 = defaultdict(set)
    for x,y in edges:
        d1[x].add(y)
        d2[y].add(x)

    degs = [0] * n
    vis = [False] * n 
    q = deque([])
    for i in range(n):
        degs[i] = len(list(d2[i]))
        if degs[i] == 0:
            q.append(i)
            vis[i] = True
    # print(degs)
    while q:
        cur = q.popleft()
        for v in d1[cur]:
            degs[v] -= 1
            if degs[v] == 0 and not vis[v]:
                q.append(v)
                vis[v] = True 
    # print(vis)
    for flag in vis:
        if not flag:
            return False 
    return True 

if __name__ == "__main__":
    n = 20
    edges = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    # n = 3
    # edges = [[0,1],[1,2]]
    print(TopologicalSorting(n,edges))
    