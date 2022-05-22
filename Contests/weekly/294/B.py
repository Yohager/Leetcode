class Solution:
    def maximumBags(self, c: List[int], r: List[int], a: int) -> int:
        diff = [x-y for x,y in zip(c,r)]
        # print(diff)
        diff.sort()
        idx = 0
        ans = 0
        while idx < len(diff) and a >= 0:
            if diff[idx] == 0:
                ans += 1
            else:
                if a < diff[idx]:
                    break 
                else:
                    a -= diff[idx]
                    ans += 1
            idx += 1
        return ans 
            