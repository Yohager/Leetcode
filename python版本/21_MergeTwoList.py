# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        new_linklist = ListNode(0)
        result = new_linklist
        while (l1 != None and l2 != None):
            temp = ListNode(0)
            if (l1.val < l2.val):
                temp.val = l1.val
                l1 = l1.next
            else:
                temp.val = l2.val
                l2 = l2.next
            new_linklist.next = temp
            new_linklist = new_linklist.next
        if (l1 != None):
            new_linklist.next = l1
        if (l2 != None):
            new_linklist.next = l2
        return result.next

