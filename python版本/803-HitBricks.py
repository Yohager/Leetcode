class UFS():
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
    
    def get_size_of_set(self,x):
        #获取当前x所在联通块的大小
        return self.size_of_set[self.find(x)]
    
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.size_of_set[root_y] += self.size_of_set[root_x]
            del self.size_of_set[root_x]
    
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1


class Solution:
    def __init__(self):
        self.CEILING = (-1,-1)
        self.DIRECTION = ((1,0),(-1,0),(0,1),(0,-1))
    
    def init_ufs(self,ufs,m,n,grid,hits):
        ufs.add(self.CEILING)

        for x,y in hits:
            grid[x][y] -= 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ufs.add((i,j))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.merge_neighbors(ufs,m,n,grid,i,j)
        
        for j in range(n):
            if grid[0][j] == 1:
                ufs.merge((0,j),self.CEILING)
    
    def is_valid(self,x,y,grid,m,n):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
    
    def merge_neighbors(self,ufs,m,n,grid,x,y):
        for j,k in self.DIRECTION:
            nx,ny = x+j,y+k
            if not self.is_valid(nx,ny,grid,m,n):
                continue
            ufs.merge((x,y),(nx,ny))

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        ufs = UFS()
        m,n = len(grid),len(grid[0])
        res = [0] * len(hits)

        self.init_ufs(ufs,m,n,grid,hits)

        for i in range(len(hits)-1,-1,-1):
            x,y = hits[i][0],hits[i][1]

            grid[x][y] += 1

            if grid[x][y] != 1:
                continue
            
            after_hits = ufs.get_size_of_set(self.CEILING)
            ufs.add((x,y))
            self.merge_neighbors(ufs,m,n,grid,x,y)
            if x == 0:
                ufs.merge((x,y),self.CEILING)
            
            if ufs.is_connected((x,y),self.CEILING):
                before_hits = ufs.get_size_of_set(self.CEILING)
                res[i] = before_hits - after_hits - 1
        return res














    