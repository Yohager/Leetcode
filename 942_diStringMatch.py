class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        A_str = list(range(N+1))
        print(A_str)
        I_num = 0
        D_num = 0
        for i in S:
            if i == 'I':
                I_num += 1
            if i == 'D':
                D_num += 1
        #print(I_num,D_num)
        if I_num >= D_num:
            


test = Solution
string_test = 'IDID'
result = test.diStringMatch(test,string_test)
