# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(None)
        res = ans 
        ptr = head.next
        arr = []
        cur = 0
        while ptr:
            if ptr.val == 0:
                # arr.append(cur)
                node = ListNode(cur)
                ans.next = node 
                ans = ans.next 
                cur = 0
            else:
                cur += ptr.val 
            ptr = ptr.next 
        return res.next 
        
                
                
                