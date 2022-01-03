class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        l = len(s)
        d = {}
        d['L'] = (0,-1)
        d['R'] = (0,1)
        d['U'] = (-1,0)
        d['D'] = (1,0)
        ans = [0] * l 
        for i in range(l):
            tmp = s[i:]
            # print(tmp)
            cur_x,cur_y = startPos[0], startPos[1]
            cur_l = len(tmp)
            idx = 0
            while idx < cur_l and 0 <= cur_x < n and 0 <= cur_y < n:
                move = d[tmp[idx]]
                cur_x += move[0]
                cur_y += move[1]
                if cur_x >= n or cur_x < 0 or cur_y >= n or cur_y < 0:
                    break 
                idx += 1 
            ans[i] = idx 
        return ans 
            
                
            