'''
给定节点的个数和边的集合
'''
import collections
def topologicalsorting(n,edges):
    d = collections.defaultdict(set)
    for x,y in edges:
        d[x].add(y)
    deg = [float('inf')] * n 
    visited = [False] * n 
    for x in d:
        deg[x] = len(d[x])
    #print(deg)
    queue = []
    for i in range(n):
        if deg[i] <= 1:
            queue.append(i)
            visited[i] = True
    while queue:
        tmp = queue.pop(0)
        #弹出队首元素 
        for e in d[tmp]:
            deg[e] -= 1
            if deg[e] == 1 and not visited[e]:
                queue.append(e)
                visited[e] == True 
    for flag in visited:
        if flag == False:
            return False 
    return True 


if __name__ == "__main__":
    n = 20
    edges = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    print(topologicalsorting(n,edges))
