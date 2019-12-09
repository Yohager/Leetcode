# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        arr = []
        for linklist in lists:
            while (linklist != None and linklist.next != None):
                arr.append(linklist.val)
                linklist = linklist.next
        arr.sort()
        new = ListNode(arr[0])
        result = new
        for i in range(1,len(arr)):
            temp = ListNode(arr[i])
            new.next = temp
            new = new.next
        return result


