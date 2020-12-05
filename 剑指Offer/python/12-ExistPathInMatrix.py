class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0: return False
        if len(word) == 0: return True
        def dfs(i,j,k):
            #给出递归的返回条件
            if not (0<= i < len(board)) or not (0<=j<len(board[0])) or (board[i][j] != word[k]):
                return False
            #返回true的条件是如果找到了最后一个
            if  (k==len(word)-1):
                return True
            #递归寻找上下左右是否有满足条件的结果
            board[i][j] = 0
            result = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            board[i][j] = word[k]
            return result

        length = len(board)
        width = len(board[0])
        for i in range(length):
            for j in range(width):
                if dfs(i,j,0):
                    return True
        return False

