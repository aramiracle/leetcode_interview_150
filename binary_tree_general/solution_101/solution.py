class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        Determines whether a binary tree is symmetric around its center.

        Args:
            root (TreeNode | None): The root node of the binary tree.

        Returns:
            bool: True if the tree is symmetric, False otherwise.
        """
        if not root:
            return True

        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val
                and is_mirror(t1.left, t2.right)
                and is_mirror(t1.right, t2.left)
            )

        return is_mirror(root.left, root.right)
