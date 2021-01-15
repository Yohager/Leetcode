class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(n+1))
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        
        def union(j,k):
            parents[find(j)] = find(k)

        for j,k in edges:
            if find(j) != find(k):
                union(j,k)
            else:
                return [j,k]

        return []