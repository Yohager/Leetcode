
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins < costs[0]:
            return 0
        cnt = 0
        tmp = 0
        for i in range(len(costs)):
            if tmp + costs[i] > coins:
                break
            tmp += costs[i]
            cnt += 1
        return cnt