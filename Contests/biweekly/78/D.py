class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        if s.count(s[0]) == len(s): return 0 
        diff = [[0]*26 for _ in range(26)]
        diff_b = [[-inf]*26 for _ in range(26)]
        
        for ch in s:
            ch = ord(ch) - ord('a')
            for i in range(26):
                if i == ch:
                    continue 
                # a = ch, b = i 
                diff[ch][i] += 1
                diff_b[ch][i] += 1

                # a = i, b = ch 
                diff[i][ch] -= 1
                diff_b[i][ch] = diff[i][ch]
                if diff[i][ch] < 0:
                    diff[i][ch] = 0 
                ans = max(ans,diff_b[i][ch],diff_b[ch][i])
        return ans 