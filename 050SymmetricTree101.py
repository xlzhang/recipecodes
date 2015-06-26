# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
	def isSymmetric(self, root):
		if not root:
			return True
		return self.SymmetricTree(root.left,root.right)
		
	def SymmetricTree(self,left,right):
		if not left and not right:
			return True
		elif (left and not right) or (right and not left) :
			return False
		return (left.val==right.val) and self.SymmetricTree(left.left, right.right) and self.SymmetricTree(left.right, right.left)

		
	def valid(self,ls):
		if ls == ls[::-1]:
			return True
		return False
	
	def isSymmetric(self, root):
		if not root:
			return True
		q1 = []
		q1.append(root)
		q2 = []
		ls = []
		while len(q1) !=0 or len(q2) != 0:
			if len(q1) !=0:
				while len(q1) !=0:
					node = q1.pop()
					ls.append(node.val)
					if node.val != -999:
						if node.left:
							q2.append(node.left)
						else:
							q2.append(TreeNode(-999))
						if node.right:
							q2.append(node.right)
						else:
							q2.append(TreeNode(-999))
				if self.valid(ls) == False:
					return False
				else:
					ls = []
			else:
				while len(q2) !=0:
					node = q2.pop()
					ls.append(node.val)
					if node.val != -999:
						if node.left:
							q1.append(node.left)
						else:
							q1.append(TreeNode(-999))
						if node.right:
							q1.append(node.right)
						else:
							q1.append(TreeNode(-999))
				if self.valid(ls) == False:
					return False
				else:
					ls =[]
		return True
		
		
a = TreeNode(1)
a.right = TreeNode(2)
a.left = TreeNode(2)
b = Solution()
c = b.isSymmetric(a)
print c	
