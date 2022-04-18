class Solution:
    def minCostSetTime(self, s: int, mc: int, pc: int, tar: int) -> int:
        def mv_func(ch):
            ans = 0
            for i in range(len(ch)-1):
                if ch[i+1] == ch[i]:
                    ans += 1
            return ans 
        
        def cal_cnt(t,ch1):
            res = 0
            pn,mn = len(ch1), len(ch1)
            tch = t + ch1
            diff = mv_func(tch)
            return pn * pc + (mn-diff) * mc
        mins = tar // 60 
        left = tar % 60 
        '''
        1-59 或者 5980 - 6039之间
        只能表示为00XX或者9940-9999
        '''
        # 特殊处理这两种情况：
        if tar < 10:
            pu_cnt = 1
            mv_cnt = 0
            if s != int(str(tar)[0]):
                mv_cnt += 1
            # if str(tar)[0] != str(tar)[1]:
            #     mv_cnt += 1
            return pu_cnt * pc + mv_cnt * mc 
        elif tar <= 59:
            # 只能表示为一种方式
            pu_cnt = 2
            mv_cnt = 0
            if s != int(str(tar)[0]):
                mv_cnt += 1
            if str(tar)[0] != str(tar)[1]:
                mv_cnt += 1
            return pu_cnt * pc + mv_cnt * mc 
        elif tar >= 5980:
            # pn_cnt = 4
            # mv_cnt = 4 
            # cur = str(s) + str(tar)
            # for i in range(len(cur)-1):
            #     if cur[i+1] == cur[i]:
            #         mv_cnt -= 1
            # return pn_cnt * pc + mv_cnt * mc 
            cur = '99' + str(tar-(99*60))
            #print(cur)
            return cal_cnt(str(s),cur)
        else:
            # 如果余数小于39则可以表示为两种方式
            if left > 39:
                # 余数大于39 则无法表示为两种形式
                tmp = str(mins) + str(left) # tmp表示需要输入的结果
                pn_cnt = len(tmp)
                cur = str(s) + tmp 
                mv_cnt = pn_cnt 
                for i in range(len(cur)-1):
                    if cur[i+1] == cur[i]:
                        mv_cnt -= 1
                return pn_cnt * pc + mv_cnt * mc 
            else:
                # 余数小于39 表示为两种形式
                tmp1, tmp2  = [],[]
                tmp1.append(str(mins))
                tmp1.append(str(left))
                tmp2.append(str(mins-1))
                tmp2.append(str(left+60))
                # 两种特殊情况
                # tmp1的left小于10
                if int(tmp1[1]) < 10:
                    tmp1[1] = '0'+str(left)
                if int(tmp2[0]) == 0:
                    tmp2.pop(0)
                c1,c2 = ''.join(tmp1),''.join(tmp2)
                print(c1,c2)
                return min(cal_cnt(str(s),c1),cal_cnt(str(s),c2))
                
                
            
            
                
            
                
                