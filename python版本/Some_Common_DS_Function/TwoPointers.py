import collections
def FindSubStrings(s):
    n = len(s)
    l,r = 0,0
    counter = collections.Counter()
    ans = 0
    while r < n:
        counter[s[r]] += 1
        while True: #修改为区间不符合题意(l,r)
            counter[s[l]] -= 1
            l += 1
        ans = max(ans,r-l+1)
        r += 1
    return ans