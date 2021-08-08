class Solution:
    def minSwaps(self, s: str) -> int:
        '''
        本质上还是要读清楚题目要求的意思
        这个题目本质在于：对于每一个]来说，如果出现在了左边，那么就意味着一定是需要进行交换的，依据这个性质就可以做
        定义一个中间变量：cnt，遇到]就-1遇到[就+1，一旦为负表示一定需要一次交换，交换过后我们会发现一定有cnt的值+2
        每一次计数即可
        '''
        # ans, cnt = 0,0
        # for w in s:
        #     if w =='[': cnt += 1
        #     elif w == ']': cnt -= 1
        #     while cnt < 0:
        #         cnt += 2
        #         #交换一次
        #         ans += 1
        # return ans 
        '''
        当然还有另外一个方法，根据栈进行括号匹配，然后最后剩下的所有的都是右括号在左边，左括号在右边
        首先进行括号匹配
        '''
        stk = []
        for w in s:
            if w == '[':
                stk.append(w)
            else:
                if len(stk) > 0 and stk[-1] == '[':
                    #匹配到了就直接消去
                    stk.pop()
                else:
                    #遇到无法匹配的情况直接将]放进去
                    stk.append(w)
        return (len(stk)//2 + 1) // 2
        

