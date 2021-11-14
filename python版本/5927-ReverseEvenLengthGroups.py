# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        tmp = head
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next 
        
        n = len(arr)
        groups = 0
        for x in range(1,1000):
            if (x**2 + x) // 2 >= n:
                groups = x 
                break 
        # 共有groups组
        # 第2,4,...,(2k)组需要翻转
        nums = []
        for i in range(groups-1):
            nums.append(i+1)
        nums.append(n-sum(nums))
        # while idx < groups+1:
        #     if idx % 2 == 0:
        #         if j + idx < n:
        #             res.append(list(reversed(arr[j:j+idx])))
        #             j += idx 
        #         else:
        #             res.append(list(reversed(arr[j:n])))
        #     else:
        #         if j + idx < n:
        #             res.append(arr[j:j+idx])
        #             j += idx
        #         else:
        #             res.append(arr[j:n])
        #     idx += 1
        # print(res)
        ans = []
        j = 0
        for num in nums:
            if num % 2 == 0:
                ans += list(reversed(arr[j:j+num]))
            else:
                ans += arr[j:j+num]
            j += num
        new_node = ListNode(ans[0])
        tmp_node = new_node
        k = 1
        while k < n:
            temp = ListNode(ans[k])
            tmp_node.next = temp 
            tmp_node = tmp_node.next 
            k += 1
        return new_node
        