class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = len(A)
        ans = []
        tmp = ''

        for i in A:
            tmp += str(i)
            ans.append(True) if (int(tmp,2) % 5 == 0) else ans.append(False)
        return ans