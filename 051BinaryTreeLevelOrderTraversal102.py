# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
		q1 = []
		q2 = []
		ls = []
		ret = []
		if not root:
			return ret
		q1.append(root)
		while 1:
			while len(q1) != 0:
				node = q1.pop(0)
				ls.append(node.val)
				if node.left:
					q2.append(node.left)
				if node.right:
					q2.append(node.right)
			ret.append(ls)
			ls = []
			q1 = q2
			q2 = []
			if len(q1) == 0:
				return ret
#### the idea is using q1 to save the current level nodes and using q2 to save
#### their left and right node and then using ls to save the current nodes' values
#### and then append ls to ret.
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
b = Solution()
c = b.levelOrder(a)
print c	
					
