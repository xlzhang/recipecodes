# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
	def isBalanced(self, root):
		if not root:
			return True
		l = self.getHeight(root.left)
		r = self.getHeight(root.right)
		return abs(l-r)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
			
	def getHeight(self, root):
		if not root:
			return 0
		return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		
		
a = TreeNode(1)
a.left = None
a.right = TreeNode(2)
a.right.left = TreeNode(3)
b = Solution()
c = b.isBalanced(a)
print c
