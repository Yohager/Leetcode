class Solution:
    def maximumBobPoints(self, na: int, a: List[int]) -> List[int]:
        maxscore = 0
        res = None
        n = len(a)
        for i in range(1 << n):
            cur = []
            cnt = na
            score = 0
            for j in range(n):
                if (i>>j) & 1:
                    cur.append(j)
            # cur表示选出的那些位置
            arrows = [0]*n
            for c in cur:
                arrows[c] = a[c] + 1
                cnt -= a[c]+1
                score += c 
            if cnt < 0:
                continue 
            else:
                arrows[0] += cnt 
            if score > maxscore:
                maxscore = score
                res = arrows 
        return res 
                
        
            
        