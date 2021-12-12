class Solution:
    def minimumRefill(self, plants: List[int], cA: int, cB: int) -> int:
        n = len(plants)
        # print(n)
        ans = 0
        ia,ib = 0,n-1
        a,b = cA,cB
        while ia <= ib:
            # print(ia,ib)
            if ia == ib:
                if a >= plants[ia]:
                    break 
                else:
                    if b >= plants[ib]:
                        break 
                    else:
                        a = cA
                        ans += 1
                        break 
            if a >= plants[ia]:
                a -= plants[ia]
            else:
                ans += 1
                a = cA
                a -= plants[ia]
            if b >= plants[ib]:
                b -= plants[ib]
            else:
                ans += 1
                b = cB
                b -= plants[ib]
            ia += 1
            ib -= 1
            
        return ans 
        