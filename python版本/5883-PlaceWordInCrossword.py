class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        #检查单个区间的情况
        def check_word(v,w):
            if len(v) != len(w):
                return False
            for i in range(len(v)):
                if v[i] != w[i]:
                    if v[i] != ' ':
                        return False 
            return True
        #检查整个zone
        def check(arr):
            m = len(arr)
            n = len(arr[0])
            flag = False
            for i in range(m):
                #按行找#之间的位置
                tmp = []
                for j in range(n):
                    if arr[i][j] == '#':
                        tmp.append(j)
                #tmp存储了每一行中所有的#号出现的位置
                #print("all # is here:",tmp)
                if not tmp:
                    #这种情况下表示当前一行没有出现#则判断当前一整行是否能放
                    if check_word(arr[i],word):
                        return True 
                elif len(tmp) == 1:
                    if tmp[0] == 0:
                        if check_word(arr[i][1:],word):
                            return True 
                    elif tmp[0] == n-1:
                        if check_word(arr[i][:-1],word):
                            return True 
                    else:
                        if check_word(arr[i][:tmp[0]],word) or check_word(arr[i][tmp[0]+1:],word):
                            return True 
                else:
                    tl = len(tmp)
                    for x in range(1,tl):
                        if check_word(arr[i][tmp[x-1]+1:tmp[x]],word):
                            return True 
                    if tmp[0] != 0:
                        #check最左边的情况
                        if check_word(arr[i][:tmp[0]],word):
                            return True 
                    if tmp[-1] != n-1:
                        if check_word(arr[i][tmp[-1]+1:],word):
                            return True 
            return False 

        def func(arr):
            temp = []
            for x in arr:
                temp.append(x[::-1])
            return temp 

        if check(board) or check(func(board)) or check(list(map(list,zip(*board)))[::-1]) or check(func(list(map(list,zip(*board)))[::-1])):
            return True
        return False 



                        
