class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def hdiv(dividend, divisor, precision=0):
            a = dividend  
            b = divisor
            #有负数的话做个标记  
            if (a > 0 and b > 0) or (a < 0 and b < 0):  
                flag = 1  
            else:  
                flag = -1 
            
            #变为正数，防止取模的时候有影响  
            a = abs(a)  
            b = abs(b)  
        
            quotient = a // b  
            remainder = a % b  
            
            if remainder == 0:  
                return str(quotient * flag)
            
            ans = [str(quotient), '.']
            repeats = dict()
            i = 0  
            while i < precision:  
                a = remainder * 10  
                quotient = a // b  
                remainder = a % b
                if a in repeats:
                    ans.insert(repeats[a], '(')
                    ans.append(')')
                    break
                ans.append(str(quotient))
                repeats[a] = i + 2
                if remainder == 0:  
                    break  
                i += 1  
            
            if precision == 0:  
                ans.pop(1)

            if flag == -1:  
                return '-' + ''.join(ans) 
            
            return ''.join(ans)
        
        return hdiv(numerator, denominator, 10000)