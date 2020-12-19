class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        count = 0
        i = 0
        while (i < len(s)):
            #如果遇到的是左括号就压栈一个左括号等待右括号的出现
            if s[i] == '(':
                count += 1
                i += 1
            #否则遇到的一定是右括号
            else:
                #如果栈内有左括号我们就pop出去一个，因为这是考虑我们遇到的是右括号所以存在两种情况，一种是有两个右括号将其pop出去，另一种是需要补了之后将左括号pop出去，反正都要pop出去一个
                if count > 0:
                    count -= 1
                #如果栈内为空，那么一定表示从当前字符开始这个右括号已经没办法消化了一定需要添加一个左括号才能消化
                else:
                    result += 1
                #如果当前是右括号且下一个也是右括号我们就将直接跳过这两个右括号，因为前面已经左括号pop过一次了所以不需要再pop了
                if (i < len(s)-1 and s[i+1] == ")"):
                    i += 2
                #这种情况下遇到的是")("，也就是说前面这个右括号是还必须要再来一个右括号才能消化了，所以需要补一个右括号
                else:
                    result += 1
                    i += 1
        #如果发现栈内还有元素的话就需要在一个左括号对应添加两个右括号
        if count > 0:
            result = result + count*2
        return result


            