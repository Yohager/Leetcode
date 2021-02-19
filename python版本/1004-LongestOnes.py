class Solution:
    def longestOnes(self, A, K: int) -> int:
        n = len(A)
        if K >= n:
            return n
        l,r = 0,0
        ans = 0
        tmp = 0
        while r < n:
            if A[r] == 0:
                tmp += 1
            while tmp > K:
                if A[l] == 0:
                    tmp -= 1
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans



if __name__ == "__main__":
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 3
    B = []
    print(Solution.longestOnes(Solution,A,K))