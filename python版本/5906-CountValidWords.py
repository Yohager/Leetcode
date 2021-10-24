class Solution:
    def countValidWords(self,s: str) -> int:
        temp = ['!',',','.']
        arr = s.split()
        ans = 0
        def func(a):
            tmp = a.index('-')
            if tmp == 0 or tmp == len(a)-1:
                return False
            for i in range(tmp):
                if not a[i].isalpha():
                    return False
            for j in range(tmp+1,len(a)):
                if not a[j].isalpha():
                    return False
            return True
        
        def func3(d):
            for dx in d:
                if not dx.isalpha():
                    return False
            return True
        
        for x in arr:
            if x.isalpha():
                ans += 1
                continue
            if '-' in x:
                if func(x):
                    ans += 1
                    continue
            if x[-1] in temp:
                c = x[:-1]
                if func3(c):
                    ans += 1
                    continue
            if x[-1] in temp and '-' in x:
                d = x[:-1]
                if func(d):
                    ans += 1
                    continue
        return ans 