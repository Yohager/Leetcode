# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        new = ans
        while l1 != None and l2 != None:
            temp = None
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            ans.next = temp
            ans = ans.next
        if l1 != None:
            ans.next = l1
        if l2 != None:
            ans.next = l2
        return new.next