# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
		
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(-999)
b = Solution()
c = b.invertTree(a)
print c.val, c.left.val, c.right.val
