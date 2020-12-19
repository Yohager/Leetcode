class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        #result = [[0 for _ in range(len(A))] for _in range(len(A[0]))]
        result = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            result.append(temp)
        return result
        #return zip(*A)

                