class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        c = collections.Counter(s)
        if n % 2 == 0:
            if c['0'] != c['1']:
                return -1
        else:
            if abs(c['0']-c['1']) != 1:
                return -1
        cnt1,cnt2 = 0,0
        d1,d2,k1,k2 = 0,0,0,0
        for i in range(n):
            if s[i] != str(i%2):
                cnt1 += 1
                if s[i] == '0':
                    #将0变成了1
                    d1 += 1
                else:
                    d2 += 1
            else:
                cnt2 += 1
                if s[i] == '0':
                    #将0变成了1
                    k1 += 1
                else:
                    k2 += 1
        print(d1,d2,k1,k2)
        print(cnt1,cnt2)
        if d1 == d2 and k1 == k2:
            ans = min(cnt1,cnt2)
        elif d1 != d2:
            ans = cnt2
        elif k1 != k2:
            ans = cnt1
        return int(ans/2)