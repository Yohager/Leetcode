class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        base = 1
        n = len(encoded)
        for i in range(2,n+2):
            base ^= i 
        for j in range(1,n,2):
            base ^= encoded[j]

        ans = [base]
        for i in range(n):
            temp = ans[i] ^ encoded[i]
            ans.append(temp)
        return ans