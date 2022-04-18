class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s = set()
        for sw in startWords:
            tmp = ''.join(sorted(sw))
            s.add(tmp)
        # print(s)
        ans = 0
        for tw in targetWords:
            cur = sorted(tw)
            for i in range(len(cur)):
                if ''.join(cur[:i]+cur[i+1:]) in s:
                    # print(''.join(cur))
                    ans += 1
                    break 
        return ans 