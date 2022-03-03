class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        ans = ''
        if num > 0:
            nums = list(map(int,list(str(num))))
            nums.sort()
            if nums[0] == 0:
                # 找到第一个非0的数调换位置
                for i in range(len(nums)):
                    if nums[i] != 0:
                        nums[0],nums[i] = nums[i], nums[0]
                        break 
                ans += ''.join(list(map(str,nums)))
            else:
                ans += ''.join(list(map(str,nums)))
        else:
            nums = list(map(int,list(str(abs(num)))))
            nums.sort(reverse=True)
            ans = '-'
            ans += ''.join(list(map(str,nums)))
        return int(ans) 