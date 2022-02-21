class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        ans = 0
        a1 = max(num1,num2)
        a2 = min(num1,num2)
        while True:
            diff = a1 - a2
            #print(diff)
            ans += 1
            if diff == 0:
                break
            a1 -= a2
            if a1 < a2:
                a1,a2 = a2,a1
            
        return ans 
            