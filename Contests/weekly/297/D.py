class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        # f[i][j]表示有多少个首字母为i的字符串，将首字母替换为j后没有在hash表中出现过
        f = [[0]*26 for _ in range(26)]
        d = set()
        for x in ideas:
            d.add(x)
        for x in ideas:
            a = ord(x[0]) - ord('a')
            for i in range(26):
                cur = chr(i+ord('a')) + x[1:]
                if cur not in d:
                    f[a][i] += 1
        ans = 0
        for x in ideas:
            a = ord(x[0]) - ord('a')
            for i in range(26):
                cur = chr(i+ord('a')) + x[1:]
                if cur not in d:
                    ans += f[i][a]
        return ans