class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        if sum(costs) < coins:
            return len(costs)
        if min(costs) > coins:
            return 0
        for i in costs:
            if coins <= 0:
                break 
            if coins >= i:
                coins -= i 
                res += 1
            else:
                break
        return res 
