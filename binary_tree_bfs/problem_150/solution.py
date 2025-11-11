class Solution(object):
    def averageOfLevels(self, root):
        """
        Calculates the average value of the nodes on each level of a binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            List[float]: A list of floating-point numbers where each element 
                         represents the average value of nodes at that level.
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_sum = 0
            level_count = len(queue)
            next_level = []
            
            for node in queue:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            result.append(level_sum / float(level_count))
            queue = next_level
        
        return result
