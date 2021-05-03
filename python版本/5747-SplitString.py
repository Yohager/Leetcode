class Solution:
    def splitString(self, newstr) -> bool:
        if len(newstr) == 1:
            return False
        n = len(newstr)
        #print(newstr)
        for i in range(1,n):
            #表示划分为多长的字符串
            tmp = int(newstr[:i])
            a = [newstr[:i]]
            l,r = i,i+1
            while r <= n:
                if tmp - 1 == 0:
                    #表示此时后续的所有的子串只能组成一个值
                    if int(newstr[l:]) == 0:
                        a.append(newstr[l:])
                    break
                else:
                    if int(newstr[l:r]) == tmp - 1:
                        tmp -= 1
                        a.append(newstr[l:r])
                        l = r
                    r += 1
            
            #print(a)
            if "".join(a) == newstr:
                return True

        return False