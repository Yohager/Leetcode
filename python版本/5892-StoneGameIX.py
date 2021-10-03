class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def check(act,d):
            if d[act] > 0:
                d[act] -= 1
                state = act 
                while True:
                    if d[state] > 0:
                        d[state] -= 1
                        state = 3 - state 
                    elif d[0] > 0:
                        d[0] -= 1
                    else:
                        return True 
                    
                    if d[0]+d[1]+d[2] == 0:
                        return False 
                    
                    if d[state] > 0:
                        d[state] -= 1
                        state = 3 - state 
                    elif d[0] > 0:
                        d[0] -= 1
                    else:
                        return False
                    
                    if d[0]+d[1]+d[2] == 0:
                        return False 

            return False 
        
        n = len(stones)
        if n == 1:
            return False
        c = {0:0,1:0,2:0}
        for s in stones:
            c[s%3] += 1
        Flag1 = check(1,c)
        c = {0:0,1:0,2:0}
        for s in stones:
            c[s%3] += 1
        Flag2 = check(2,c)
        return Flag1 or Flag2