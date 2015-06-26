# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
	def levelOrderBottom(self, root):
		res = []
		if root == None:
			return res
		q = []
		q.append([root, 1])
		while len(q) != 0:
			node, dep = q.pop()
			if len(res) < dep:
				res.append([node.val])
			else:
				res[dep-1].append(node.val)
			if node.right != None:
				q.append([node.right, dep + 1])        
			if node.left != None:
				q.append([node.left, dep + 1])
		return res[::-1]

		
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
				return ret[::-1]
		
	
a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)
b = Solution()
c = b.levelOrderBottom(a)
print c	
