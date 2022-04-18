class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b1 = bin(start)[2:]
        b2 = bin(goal)[2:]
        ans = 0
        max_len = max(len(b1),len(b2))
        b1 = b1.rjust(max_len,'0')
        b2 = b2.rjust(max_len,'0')
        # print(b1,b2)
        for x,y in zip(b1,b2):
            if x != y:
                ans += 1
                
        return ans 