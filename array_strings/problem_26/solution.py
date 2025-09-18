class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns 
        the number of unique elements.

        Args:
            nums (List[int]): A sorted list of integers (non-decreasing order).

        Returns:
            int: The number of unique elements remaining in `nums` after duplicates are removed.
        """
        count = 0
        check_element = None
        for idx, element in enumerate(nums):
            if check_element == element:
                count -= 1
            else:
                nums[count] = nums[idx]
            count += 1
            check_element = element
        return count
