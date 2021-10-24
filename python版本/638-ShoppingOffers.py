class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(None)
        def dfs(left):
            total = sum(price[i]*num for i,num in enumerate(left))
            #print(total)
            if not total:
                return 0
            for s in special:
                nex = tuple((x-y for x,y in zip(left,s)))
                if all(diff >= 0 for diff in nex):
                    total = min(total,dfs(nex)+s[-1])
            return total 
        
        return dfs(tuple(needs))