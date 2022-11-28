# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next 
        ans = [tmp[-1]]
        n = len(tmp)
        for i in range(n-2,-1,-1):
            if tmp[i] >= ans[-1]:
                ans.append(tmp[i])
        res = ListNode(-1)
        new_head = res 
        for i in range(len(ans)-1,-1,-1):
            cur = ListNode(ans[i])
            new_head.next = cur 
            new_head = new_head.next 
        return res.next 