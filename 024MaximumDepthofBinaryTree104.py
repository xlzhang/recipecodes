# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param {TreeNode} root
	# @return {integer}
	def maxDepth(self, root):
		if root == None:
			return 0
		ldepth = self.maxDepth(root.left)
		rdepth = self.maxDepth(root.right)
		return max(ldepth+1, rdepth+1)
	
def main():
	a = TreeNode(1)
	a.left = TreeNode(2)
	a.right = TreeNode(3)
	a.left.left = TreeNode(4)
	a.left.right = TreeNode(5)
	a.left.left.left = TreeNode(6)
	b = Solution()
	c = b.maxDepth(a)
	print c
if __name__ == "__main__":
	main()
	
	
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return false;
        }
        int ret = 0;
        int depth = 0;
        auto cur = root;
        while (cur) {
            if (!cur->left) {
                cur = cur->right;
                ++depth;
            }
            else {
                auto prev = cur->left;
                int dist = 1;
                while (prev->right && prev->right != cur) {
                    prev = prev->right;
                    ++dist;
                }
                if (prev->right) {
                    prev->right = nullptr;
                    cur = cur->right;
                    ret = max(ret, depth);
                    depth -= dist;
                }
                else {
                    prev->right = cur;
                    cur = cur->left;
                    ++depth;
                }
            }
        }
        return max(ret, depth);
    }
};
