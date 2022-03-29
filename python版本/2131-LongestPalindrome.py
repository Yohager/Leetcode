class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        a = set()
        b = set()
        ans = 0
        for key in d.keys():
            if key[0] == key[1]:
                a.add(key)
            else:
                if not b:
                    b.add(key)
                else:
                    if key[::-1] in b:
                        ans += min(d[key],d[key[::-1]])
                        b.remove(key[::-1])
                    else:
                        b.add(key)
        # 对于a中，如果数量超过了2可以加入
        # 对于b中，ans已经记录了匹配的情况
        flag = False
        for x in a:
            if d[x] == 1:
                flag = True
            elif d[x] >= 2:
                # 超过两个
                if d[x] % 2 != 0:
                    flag = True
                ans += d[x]//2
        if not flag:
            return 4 * ans 
        else:
            return 4 * ans + 2