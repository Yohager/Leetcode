class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums: return ''
        if len(nums) == 1: return str(nums[0])
        compare = lambda x,y: 1 if x+y > y+x else -1
        tmp = list(map(str,nums))
        tmp.sort(key=cmp_to_key(compare))
        tmp.reverse()
        #print(tmp)
        if tmp[0] == '0':
            return '0'
        return ''.join(tmp)