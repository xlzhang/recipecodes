# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
		if head == None or head.next == None:
			return head
		rer_head = ListNode(0)
		temp_head = ListNode(0)
		temp_next = ListNode(0)
		flag = 0
		while head:
			temp_next = head.next
			temp_head = head
			if flag == 0:
				rer_head = temp_head
				rer_head.next = None
				flag = 1
			else:
				temp_head.next = rer_head
				rer_head = temp_head
			head = temp_next
		return temp_head
				
	
a = ListNode()
print a.val
a.next = ListNode(2)
b = Solution()
c = b.reverseList(a)
print c.val, c.next.val
