class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rlist = []
        dlist = []
        #先使用两个list将两个阵营的index分别存储
        #用于后续判断谁优先的问题
        for i in range(len(senate)):
            if senate[i] == "R":
                rlist.append(i)
            else:
                dlist.append(i)
        while (rlist != [] and dlist != []):
            if rlist[0] < dlist[0]:
                rlist.append(rlist[0]+len(senate))
            else:
                dlist.append(dlist[0] + len(senate))
            rlist.pop(0)
            dlist.pop(0)
        return "Dire" if dlist else "Radiant"



        