#from functools import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #分类性质的问题典型的使用hash表进行处理
        #先找到关键的用于判断是否同构的键值，然后依次判断添加
        #result = []
        dict1 = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in dict1:
                dict1[key] = [s]
            else:
                dict1[key].append(s)
        return list(dict1.values())


