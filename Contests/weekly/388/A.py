class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        idx = 0
        ret = 0
        while total > 0:
            total -= capacity[idx]
            ret += 1
            idx += 1
            # print(total, ret)
        return ret 
