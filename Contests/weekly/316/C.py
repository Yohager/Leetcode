class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        total = list(zip(nums, cost))
        n = len(total)
        total.sort()
        diff = [total[i][0]-total[i-1][0] for i in range(1,n)]
        prefix = [total[0][1]]
        for i in range(1,n):
            prefix.append(prefix[-1] + total[i][1])
        cur_cost = sum([c * (x- total[0][0]) for x, c in total])
        ans = cur_cost
        for i in range(1,n):
            # 当前以num为元素计算total cost
            cur_diff = diff[i-1]
            cur_cost += cur_diff * prefix[i-1]
            cur_cost -= cur_diff * (prefix[-1] - prefix[i-1])
            # print(prefix)
            # print(cur_diff, prefix[i-1], prefix[-1] - prefix[i-1])
            # print(cur_cost)
            ans = min(ans, cur_cost)
        return ans 