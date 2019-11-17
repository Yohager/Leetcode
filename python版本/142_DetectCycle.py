# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    	if head == None or head.next == None:
    		return False
    	slow_ptr = head
    	fast_ptr = head
    	flag = 0
    	while (fast_ptr != None and fast_ptr.next != None):
    		slow_ptr = slow_ptr.next
    		fast_ptr = fast_ptr.next.next
    		if (slow_ptr == fast_ptr):
    			flag = 1
    			break
    	if (flag == 0):
    		return False
    	temp_1 = slow_ptr
    	temp_2 = head
    	while (temp_1 != temp_2):
    		temp_1 = temp_1.next
    		temp_2 = temp_2.next
    	return temp_1