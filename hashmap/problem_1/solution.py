class Solution(object):
    def twoSum(self, nums, target):
        """
        Find indices of the two numbers in the list that add up to the target.

        Args:
            nums (List[int]): List of integers to search through.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing two indices [i, j] such that 
                       nums[i] + nums[j] == target. If multiple solutions 
                       exist, returns the first one found.
        """
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
