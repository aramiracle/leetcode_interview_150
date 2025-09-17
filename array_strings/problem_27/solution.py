class Solution:
    def removeElement(self, nums, val):
        """
        Removes all instances of `val` from the list `nums` in-place. 
        The relative order of the remaining elements may change.

        Args:
            nums (List[int]): The input list of integers.
            val (int): The value to remove from the list.

        Returns:
            int: The number of elements remaining in `nums` after removal.
        """
        k = 0
        for element in nums:
            if element != val:
                nums[k] = element
                k += 1
        return k