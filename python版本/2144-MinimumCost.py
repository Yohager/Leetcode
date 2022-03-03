class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        n = len(cost)
        free = 0
        for i in range(2,n,3):
            free += cost[i]
        return sum(cost) - free