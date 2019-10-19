# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        #使用双指针做，快指针比慢指针快n个节点
        if (head.next == None):
            return None
        number = n
        #pre_pointer = head
        fast_pointer = head
        slow_pointer = head
        count = 0
        while (number > 0 and fast_pointer != None):
            count += 1
            fast_pointer = fast_pointer.next
            number -= 1
        #这种情况下一定表示的是要删除的是第一个节点
        if (count != n):
            return head.next
        #所有的其他情况都表示的是slow指针指向的是要被删除节点的前一个节点
        else:
            while (fast_pointer.next != None):
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
            #print(slow_pointer.val)
            if (slow_pointer.next.next == None):
                slow_pointer.next = None
                return head
            temp = slow_pointer.next.next
            slow_pointer.next = None
            slow_pointer.next = temp
            return head

        