class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def add_spaces(arr):
            n = len(arr)
            length = 0
            for y in arr:
                length += len(y)
            #计算每个单词之间的dist
            ans = ''
            spaces_nums = maxWidth - length
            if n == 1:
                return arr[0] + ' '*(spaces_nums)
            if spaces_nums % (n-1) == 0:
                temp = [0]
                temp += [spaces_nums // (n-1)] * (n-1)
                for j in range(n):
                    ans += (' '*temp[j] + arr[j])
            else:
                extra = spaces_nums % (n-1)
                temp = [0] 
                temp += [spaces_nums // (n-1)] * (n-1)
                for x in range(1,extra+1):
                    temp[x] += 1
                #temp存储每个单词后需要添加的空格数量
                for j in range(n):
                    ans += (' '*temp[j] + arr[j])
            return ans 
        #每一行中存在几个单词
        l = len(words)
        res = []
        idx = 0
        while idx < l:
            cur = 0
            line = []
            while cur < maxWidth and idx < l:
                line.append(words[idx])
                cur += len(words[idx]) + 1
                idx += 1
            if cur > maxWidth+1:
                line.pop()
                idx -= 1
            res.append(line)
        final_ans = []
        for r in range(len(res)-1):
            final_ans.append(add_spaces(res[r]))
        lastline = ' '.join(res[-1])
        lastline += ' '*(maxWidth - len(lastline))
        final_ans.append(lastline)
        return final_ans

