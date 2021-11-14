class Solution:
    def decodeCiphertext(self, t: str, rows: int) -> str:
        n = len(t)
        cols = n // rows 
        m = []
        for r in range(rows):
            m.append(list(t[r*cols:(r+1)*cols]))
        ans = ''
        for col in range(cols):
            # if col != 0 and m[0][col] == ' ':
            #     break
            tmp = ''
            idx = 0
            while idx < rows and col < cols:
                tmp += m[idx][col]
                idx += 1
                col += 1
            ans += tmp
        ans = ans.rstrip()
        return ans 
                