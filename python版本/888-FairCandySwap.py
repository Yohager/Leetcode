class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) // 2
        s = set(B)
        for tmp in A:
            if diff + tmp in s:
                return [tmp, diff+tmp]