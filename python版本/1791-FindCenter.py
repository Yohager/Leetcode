class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        '''
        统计每个节点出现过的次数
        如果与其他所有节点都相连，则出现的次数为n-1
        '''
        c = Counter()
        for x,y in edges:
            c[x] += 1
            c[y] += 1
        n = len(c.keys())
        for key in c.keys():
            if c[key] == n-1:
                return key