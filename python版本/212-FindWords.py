class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word, idx, p, explored):
            if idx == len(word):
                return True
            if p in explored or p[0] < 0 or p[0] == m or p[1] < 0 or p[1] == n:
                return False
            if board[p[0]][p[1]] == word[idx]:
                explored.add(p)
                idx += 1
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    if dfs(word, idx, (p[0] + dx, p[1] + dy), explored):
                        return True
                explored.remove(p)
            return False        

        m, n = len(board), len(board[0])
        cnts = Counter()
        for i in range(m):
            for j in range(n):
                cnts[board[i][j]] += 1
        ans = []
        for word in words:
            cur = Counter(word)
            canExists = True
            for c in cur:
                if cnts[c] < cur[c]:
                    canExists = False
                    break 
            if not canExists:
                continue
            find = False
            for i in range(m):
                for j in range(n):
                    if dfs(word, 0, (i, j), set()):
                        ans.append(word)
                        find = True
                        break
                if find:
                    break
        return ans
