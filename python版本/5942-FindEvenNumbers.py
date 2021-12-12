class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        ans = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    if digits[i] == 0:
                        continue
                    tmp = 100 * digits[i] + 10 * digits[j] + digits[k]
                    if tmp % 2 == 0:
                        ans.add(int(tmp))
        return sorted(list(ans))