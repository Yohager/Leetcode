class Solution:
    def addRungs(self, r: List[int], d: int) -> int:
        diff = [r[0]]
        n = len(r)
        for i in range(1,n):
            diff.append(r[i]-r[i-1])
        ans = 0
        for x in diff:
            if x > d:
                if x % d == 0:
                    ans += int(x/d) - 1
                else:
                    ans += x // d 
        return ans 
        