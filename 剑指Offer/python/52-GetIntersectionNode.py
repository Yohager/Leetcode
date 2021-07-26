# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None 
        tmp1, tmp2 = headA, headB
        while tmp1 != tmp2:
            if tmp1 == None:
                tmp1 = headB
            else:
                tmp1 = tmp1.next
            
            if tmp2 == None:
                tmp2 = headA
            else:
                tmp2 = tmp2.next
        return tmp2
                