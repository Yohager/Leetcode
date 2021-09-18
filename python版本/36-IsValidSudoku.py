class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #首先检查每一行是否只出现了一次
        for line in board:
            c_line = collections.Counter(line)
            for x in c_line:
                if x != '.' and c_line[x] >= 2:
                    return False 
        #检查每一列是否满足条件
        for col in list(zip(*board)):
            c_col = collections.Counter(col)
            for y in c_col:
                if y != '.' and c_col[y] >= 2:
                    return False 
        #检查每一个3*3的单元
        tops = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for idx in tops:
            tmp = collections.Counter()
            for i in range(idx[0],idx[0]+3):
                for j in range(idx[1],idx[1]+3):
                    tmp[board[i][j]] += 1
            for e in tmp:
                if e != '.' and tmp[e] >= 2:
                    return False 
        return True 