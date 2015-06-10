# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
  def getIntersectionNode(self, headA, headB):
		if headA==None or headB == None:
			return None
		if headA.val == headB.val:
		    return headA
		numa = 0
		numb = 0
		tempa = headA
		tempb = headB
		while tempa:
			numa += 1
			tempa = tempa.next
		while tempb:
			numb += 1
			tempb = tempb.next
		if numa>numb:
			dif = numa-numb
			starta = headA
			startb = headB
		else:
			dif = numb-numa
			starta = headB
			startb = headA
		
		while dif >0:
			starta = starta.next
			dif -= 1
		while starta:
			if starta == startb:
				return starta
			starta = starta.next
			startb = startb.next
		return None
		
	def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        if headA == headB:
            return headA
        tempa = headA
        tempb = headB
        na = 0
        nb = 0
        while tempa:
            na += 1
            tempa = tempa.next
        while tempb:
            nb += 1
            tempb = tempb.next
        m = na + nb
        tempa = headA
        tempb = headB
        while m > 0:
            if tempa == tempb:
                return tempa
            tempa = tempa.next
            tempb = tempb.next
            if tempa == None:
                tempa = headB
            if tempb == None:
                tempb = headA
            m -= 1
        return None
        
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        if headA == headB:
            return headA
        tempa = headA
        tempb = headB
        Flag = False
        while 1:
            if tempa == tempb:
                return tempa
            tempa = tempa.next
            tempb = tempb.next
            if tempa == None:
                if Flag:
                    return None
                Flag = True
                tempa = headB
            if tempb == None:
                tempb = headA
        return None
