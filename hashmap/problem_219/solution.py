class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Determines if the array `nums` contains duplicate elements such that 
        the indices of the duplicates are at most `k` positions apart.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The maximum allowed index distance between duplicate elements.

        Returns:
            bool: 
                - True if there exists at least one pair of duplicate elements 
                  with index difference less than or equal to k.
                - False otherwise.
        """
        nums_dict = {}

        for i, num in enumerate(nums):
            if num in nums_dict:
                if i - nums_dict[num] <= k:
                    return True
                else:
                    nums_dict[num] = i
            else:
                nums_dict[num] = i
        return False
