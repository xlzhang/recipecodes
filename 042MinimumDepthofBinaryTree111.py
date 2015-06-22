# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
		if not root:
			return 0
		if not root.left and not root.right:
			return 1
		if not root.left and root.right:
		    return self.minDepth(root.right)+1
		elif not root.right and root.left:
		    return self.minDepth(root.left)+1
		else:
			a = self.minDepth(root.right)+1
			b = self.minDepth(root.left)+1
			if a>b:
				return b
			else:
				return a
			
a = TreeNode(1)
a.left = None
a.right = TreeNode(2)
b = Solution()
c = b.minDepth(a)
print c
