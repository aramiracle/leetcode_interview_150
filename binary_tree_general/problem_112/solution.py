# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        Determines if the binary tree has a root-to-leaf path such that
        the sum of the node values along the path equals targetSum.

        Args:
            root (TreeNode): The root node of the binary tree.
            targetSum (int): The target sum to check for along a root-to-leaf path.

        Returns:
            bool: True if such a path exists, otherwise False.
        """
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
