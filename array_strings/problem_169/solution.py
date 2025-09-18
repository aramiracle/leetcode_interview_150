class Solution(object):
    def majorityElement(self, nums):
        """
        Finds the majority element in the given list of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The majority element in the list.
        """
        nums_dict = {}
        for unique in set(nums):
            nums_dict[unique] = 0
        for element in nums:
            nums_dict[element] += 1
        max_value = max(nums_dict.values())
        majority_element = [x for x in nums_dict if nums_dict[x] == max_value][0]
        return majority_element