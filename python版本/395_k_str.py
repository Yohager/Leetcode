class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '':
            return 0
        counter = []
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                new_str = ''
                init_list = []
                sort_list = []
                new_str = s[i:j]
                #print(new_str)           
                for n in set(new_str):
                    init_list.append(n)
                    sort_list.append(new_str.count(n))
                dict_sort_str = dict(zip(init_list,sort_list))
                sort_new_list = sorted(dict_sort_str.items(),key=lambda x:x[1],reverse=True)
                #print(sort_new_list)
                if sort_new_list[-1][1]>=k:
                    counter.append(j-i)
        print(max(counter))
        if counter == []:
            max_counter = 0
        else:
            max_counter = max(counter)
        return max_counter

test = Solution
result = test.longestSubstring(test,"aaaaaaaaaaaaaaaabbbbbbbbbbbbaaaaaaabbbbbbbbbbbbcccccccccccdddddddddddddddddddeeeeeeeeeeeeeeefffffffffffffffgggggggggggggggggggghhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkk",20)


