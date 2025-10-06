class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        Inverts a binary tree by swapping the left and right child nodes recursively.

        Args:
            root (TreeNode | None): The root node of the binary tree to invert.

        Returns:
            TreeNode | None: The root node of the inverted binary tree.
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root