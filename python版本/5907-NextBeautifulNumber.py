class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def func(d):
            for y in d:
                if d[y] != int(y):
                    return False 
            return True
        flag = False
        ans = n+1
        while not flag:
            c = collections.Counter(str(ans))
            if func(c):
                flag = True
            ans += 1
        return ans-1
        # c = collections.Counter(str(n))
        