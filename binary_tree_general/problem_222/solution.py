class Solution(object):
    def countNodes(self, root):
        """
        Counts the total number of nodes in a binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            int: The total number of nodes in the tree. Returns 0 if the tree is empty.
        """
        if not root:
            return 0
        
        nodes = 1
        nodes += self.countNodes(root.left) + self.countNodes(root.right)

        return nodes
