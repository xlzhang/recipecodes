# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# @param {ListNode} head
	# @param {integer} n
	# @return {ListNode}
	def removeNthFromEnd(self, head, n):
		fast = head
		slow = head
		for i in range(n):
			fast = fast.next
		while fast.next:
			fast = fast.next
			slow = slow.next
		slow.next = slow.next.next
		return head

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = Solution()
c = b.removeNthFromEnd(a,2)
print c.val, c.next.val, c.next.next.val
