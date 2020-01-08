# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        nums = []
        while (temp != None):
            nums.append(temp.val)
            temp = temp.next
        i = 0
        j = len(nums) - 1
        while (i < j):
            if (nums[i] == nums[j]):
                continue
            else:
                return False
            i += 1
            j -= 1
        return True
        '''
        高端解法：快慢指针找到链表的中点，将前半链表进行翻转后与后半链表进行比较
        时间复杂度O(n)，空间复杂度O(1)
        '''