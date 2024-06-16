class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        new_hours = [x % 24 for x in hours]
        c = Counter(new_hours)
        i = 1
        ans = 0
        # print(c)
        while i <= 12:
            j = 24 - i
            if i == j:
                # print("here", c[i])
                ans += (c[i] * (c[i] - 1)) // 2
            # print(i, j, c[i], c[j])
            else:
                # print("here", c[i], c[j])
                ans += c[i] * c[j]
            i += 1
        # print(c[0])
        ans += (c[0] * (c[0] - 1)) // 2
        return ans 
