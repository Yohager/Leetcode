class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        这道题目正确的做法是DFA……
        但是应该面试不会恶心人吧，短时间画出有限状态的自动机估计有点费劲……
        '''
        try:
            float(s)
        except:
            return False

        return True
            