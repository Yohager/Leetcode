class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        t1 = list(s1.split(' '))
        t2 = list(s2.split(' '))
        #print(t1,t2)
        tmp = []
        tmp2 = []
        if len(t1) > len(t2):
            tmp = t2[:]
            tmp2 = t1[:]
        else:
            tmp = t1[:]
            tmp2 = t2[:]
        #短的是tmp长的是tmp2
        if len(tmp) == 1:
            if tmp[0] == tmp2[0] or tmp[0] == tmp2[-1]:
                return True
            else:
                return False
        n1 = len(tmp)
        n2 = len(tmp2)
        k = 0
        #从左边向右边逼近找到一个k
        while k < n1:
            if tmp[k] != tmp2[k]:
                break
            k+=1
        q1,q2 = tmp[k:],tmp2[k:]
        q1.reverse()
        q2.reverse()
        print(q1,q2)
        for i in range(len(q1)):
            if q1[i] != q2[i]:
                return False
        # if tmp[0] not in tmp2:
        #     return False
        # idx = tmp2.index(tmp[0])
        # print(idx)
        # if n2 - idx != n1:
        #     return False
        # k = 0
        # while idx < n2:
        #     if tmp2[idx] != tmp[k]:
        #         return False
        #     k += 1
        #     idx += 1
        return True