class ufs():
    def __init__(self,n):
        self.nums = n
        self.fathers = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]
        self.parts = n
    
    def GetParts(self):
        return self.parts

    def Find(self,x):
        if self.fathers[x] == x:
            return x
        else:
            self.fathers[x] = self.Find(self.fathers[x])
            return self.fathers[x]
    
    def Union(self,x,y):
        fa_x,fa_y = self.Find(x),self.Find(y)
        if self.ranks[fa_x] <= self.ranks[fa_y]:
            self.fathers[fa_x] = fa_y
            self.parts -= 1
        else:
            self.fathers[fa_y] = fa_x
            self.parts -= 1
        
        if self.ranks[fa_x] == self.ranks[fa_y] and fa_x != fa_y:
            self.ranks[fa_y] += 1
    
    def IsConnected(self,x,y):
        if self.Find(x) == self.Find(y):
            return True
        else:
            return False
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        criticalPath = []
        fakePath = []
        l = len(edges)
        #记录输入的edges的每个编号，用于最后输出时返回用
        for idx, edge in enumerate(edges):
            edge.append(idx)
        #按照权重进行排序
        edges.sort(key=lambda x:x[2])
        #这个函数用于确定删除一条边是否不改变最小生成树的权重
        #也就是用于判别一个边是不是关键边
        def kruskal_func1(num,edgeset,delete_edge):
            ans = 0
            ufs1 = ufs(num)
            for i,j in enumerate(edgeset):
                if i == delete_edge:
                    continue
                if not ufs1.IsConnected(j[0],j[1]):
                    ufs1.Union(j[0],j[1])
                    ans += j[2]
            if ufs1.GetParts() == 1:
                return ans 
            else:
                return -1
        #这个函数用于考虑这个边是不是虚假的关键边
        def kruskal_func2(num,edgeset,choose_edge):
            ans = edgeset[choose_edge][2]
            ufs2 = ufs(num)
            ufs2.Union(edgeset[choose_edge][0],edgeset[choose_edge][1])
            for k in edgeset:
                if not ufs2.IsConnected(k[0],k[1]):
                    ufs2.Union(k[0],k[1])
                    ans += k[2]
            return ans
        
        #求最小生成树的权重
        mst_groundtruth = kruskal_func1(n,edges,-1)
        #下面遍历所有的边分别判别是什么类型的边
        for index,tmp in enumerate(edges):
            not_choose_w = kruskal_func1(n,edges,index)
            if not_choose_w == -1 or not_choose_w > mst_groundtruth:
                criticalPath.append(tmp[-1])
            elif kruskal_func2(n,edges,index) == mst_groundtruth:
                fakePath.append(tmp[-1])
        return [criticalPath,fakePath]