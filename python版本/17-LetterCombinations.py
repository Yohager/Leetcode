class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = collections.defaultdict(set)
        d['2'].update({'a','b','c'})
        d['3'].update({'d','e','f'})
        d['4'].update({'g','h','i'})
        d['5'].update({'j','k','l'})
        d['6'].update({'m','n','o'})
        d['7'].update({'p','q','r','s'})
        d['8'].update({'t','u','v'})
        d['9'].update({'w','x','y','z'})
        ans = ['']
        if not digits:
            return []
        else:
            for x in digits:
                ans = [tmp + tmp2 for tmp in ans for tmp2 in d[x]] 
        return ans 