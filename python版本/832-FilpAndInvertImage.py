class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        w = len(A[0])
        for k in A:
            k.reverse()
            for i in range(w):
                k[i] = k[i] ^ 1
        #print(A)
        return A