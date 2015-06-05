# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
		if head == None:
			return head
		temp_head = head
		temp_next = temp_head.next
		while temp_head:
			if head.val == val:
				head = head.next
				temp_head = head
				if temp_head != None:
				    temp_next = temp_head.next
				else:
				    break
			elif temp_next == None:
			       break
			elif temp_next.val == val:
				temp_head.next = temp_next.next
				temp_next = temp_head.next
			else:
				temp_head = temp_head.next
				temp_next = temp_head.next
		return head
	
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
b = Solution()
c = b.removeElements(a,2)
print c.val
