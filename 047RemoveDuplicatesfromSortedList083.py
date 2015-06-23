# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        tp = head
        next_tp = tp.next
        while next_tp:
            if next_tp.val == tp.val:
                next_nt = next_tp.next
                tp.next = next_nt
                next_tp = tp.next
            else:
                tp = next_tp
                next_tp = tp.next
        return head
