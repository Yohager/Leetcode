class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        tmp = 0
        for i in s:
            if i == "L":
                tmp += 1
            elif i == 'R':
                tmp -= 1
            if tmp == 0:
                ans += 1
        return ans  