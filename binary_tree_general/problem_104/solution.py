class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        Calculate the maximum depth (height) of a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the binary tree. Returns 0 if the tree is empty.
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
