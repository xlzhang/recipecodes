# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l1.val > l2.val:
            swap = l1
            l1 = l2
            l2 = swap
            
        temp_l1 = l1
        
        while l2.next != None:
            if temp_l1.next != None:
                    if temp_l1.val <= l2.val and temp_l1.next.val > l2.val:
                        l2_next = l2.next
                        l2.next = temp_l1.next
                        temp_l1.next = l2
                        temp_l1 = l2
                        l2 = l2_next
                    else:
                        temp_l1 = temp_l1.next
        
            elif temp_l1.val <= l2.val and temp_l1.next == None:
                    temp_l1.next = l2
                    return l1
                    
        if l2.next == None:
            while 1:
                if temp_l1.next != None:
                    if temp_l1.val <= l2.val and temp_l1.next.val > l2.val:
                        l2_next = l2.next
                        l2.next = temp_l1.next
                        temp_l1.next = l2
                        temp_l1 = l2
                        l2 = l2_next
                        return l1
                    else:
                        temp_l1 = temp_l1.next
        
                elif temp_l1.val <= l2.val and temp_l1.next == None:
                    temp_l1.next = l2
                    return l1
        
        return l1
        
        
        
        
        
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        ret = ListNode(0)
        merge = ret
        while(1):
            if not l1:
                merge.next = l2
                return ret.next
            if not l2:
                merge.next = l1
                return ret.next
            if l1.val<=l2.val:
                merge.next = l1
                l1 = l1.next
            elif l1.val>l2.val:
                merge.next = l2
                l2 = l2.next
            merge = merge.next
                
