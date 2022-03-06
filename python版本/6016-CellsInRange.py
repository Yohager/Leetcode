class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        cols,cole = s[0], s[-2]
        rows,rowe = int(s[1]), int(s[-1])
        for i in range(ord(cols),ord(cole)+1):
            for j in range(rows,rowe+1):
                ans.append(chr(i)+str(j))
        return ans 