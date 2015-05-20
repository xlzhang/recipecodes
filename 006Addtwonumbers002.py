# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
            
        temp_l1 = l1
        while 1:
            if temp_l1:
                if (temp_l1.val + l2.val) < 10:
                    temp_l1.val += l2.val
                    old_temp = temp_l1
                    temp_l1 = temp_l1.next
                    old_l2 = l2
                    l2 = l2.next
                    if not l2 and temp_l1:
                        l2 = ListNode(0)
                        old_l2.next = l2
                else:
                    temp_l1.val = (temp_l1.val + l2.val - 10)
                    old_temp = temp_l1
                    temp_l1 = temp_l1.next
                    old_l2 = l2
                    l2 = l2.next
                    if l2:
                        l2.val += 1
                    else:
                        l2 = ListNode(1)
                        old_l2.next = l2
            elif l2:
                temp_l1 = ListNode(0)
                old_temp.next = temp_l1
            else:
                return l1
