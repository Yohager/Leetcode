# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    	if head == None or head.next == None:
    		return False
    	slow_ptr = head
    	fast_ptr = head.next
    	while (slow_ptr != fast_ptr):
    		if (fast_ptr == None or fast_ptr.next == None):
                #这种情况下没有环，fast指针一定先遍历完整个链表
    			return False
    		slow_ptr = slow_ptr.next
    		fast_ptr = fast_ptr.next.next
    	return True